<script setup>
import { ref, onMounted, nextTick } from 'vue'

const BASE = '/api/v1'

const health = ref(null)
const sessions = ref([])
const activeSession = ref(null)
const messages = ref([])
const error = ref(null)
const userId = ref('')
const messageText = ref('')
const chatLoading = ref(false)
const messageListEl = ref(null)

const view = ref('chat')
const quizTopic = ref('')
const quizQuestions = ref([])
const currentQIdx = ref(0)
const quizAnswer = ref('')
const quizFeedback = ref(null)
const quizLoading = ref(false)

async function api(method, path, body) {
  error.value = null
  const opts = { method, headers: { 'Content-Type': 'application/json' } }
  if (body) opts.body = JSON.stringify(body)
  const res = await fetch(BASE + path, opts)
  if (res.status === 204) return null
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || `HTTP ${res.status}`)
  return data
}

async function fetchHealth() {
  try {
    const data = await api('GET', '/health')
    health.value = data.status
  } catch {
    health.value = 'error'
  }
}

async function fetchSessions() {
  try {
    const path = userId.value ? `/sessions?user_id=${encodeURIComponent(userId.value)}` : '/sessions'
    sessions.value = await api('GET', path)
  } catch (e) {
    error.value = e.message
  }
}

async function createSession() {
  try {
    const body = userId.value ? { user_id: userId.value } : {}
    const s = await api('POST', '/sessions', body)
    sessions.value.unshift(s)
    selectSession(s)
  } catch (e) {
    error.value = e.message
  }
}

async function selectSession(s) {
  activeSession.value = s
  messages.value = []
  quizTopic.value = ''
  quizQuestions.value = []
  quizAnswer.value = ''
  quizFeedback.value = null
  currentQIdx.value = 0
  view.value = 'chat'
  try {
    const raw = await api('GET', `/sessions/${s.id}/messages`)
    messages.value = raw.map((m, i) => ({ ...m, role: i % 2 === 0 ? 'user' : 'assistant' }))
    await nextTick()
    messageListEl.value?.scrollTo(0, messageListEl.value.scrollHeight)
  } catch (e) {
    error.value = e.message
  }
}

async function deleteSession(id) {
  try {
    await api('DELETE', `/sessions/${id}`)
    sessions.value = sessions.value.filter(s => s.id !== id)
    if (activeSession.value?.id === id) {
      activeSession.value = null
      messages.value = []
    }
  } catch (e) {
    error.value = e.message
  }
}

async function sendMessage() {
  const text = messageText.value.trim()
  if (!text || !activeSession.value) return
  messageText.value = ''
  chatLoading.value = true
  try {
    const res = await api('POST', `/sessions/${activeSession.value.id}/messages`, { content: text })
    messages.value.push({ ...res.user_message, role: 'user' })
    messages.value.push({ ...res.assistant_message, role: 'assistant' })
    await nextTick()
    messageListEl.value?.scrollTo(0, messageListEl.value.scrollHeight)
  } catch (e) {
    error.value = e.message
  } finally {
    chatLoading.value = false
  }
}

async function generateQuiz() {
  const topic = quizTopic.value.trim()
  if (!topic || !activeSession.value) return
  quizLoading.value = true
  quizQuestions.value = []
  quizFeedback.value = null
  currentQIdx.value = 0
  quizAnswer.value = ''
  try {
    const res = await api('POST', `/sessions/${activeSession.value.id}/quiz`, { topic })
    quizQuestions.value = res.questions
  } catch (e) {
    error.value = e.message
  } finally {
    quizLoading.value = false
  }
}

function submitAnswer() {
  if (!quizAnswer.value) return
  quizAnswer.value = ''
  if (currentQIdx.value < quizQuestions.value.length - 1) {
    currentQIdx.value++
  } else {
    quizFeedback.value = 'Quiz completed!'
  }
}

onMounted(() => {
  fetchHealth()
  fetchSessions()
})
</script>

<template>
  <div class="app">
    <header>
      <span class="logo">ESBot</span>
      <span
        data-testid="health-status"
        :class="['badge', 'err', { hidden: health === 'ok' }]"
      >{{ health === null ? '…' : 'Backend offline' }}</span>
    </header>

    <div
      v-if="error"
      data-testid="error-banner"
      class="error-banner"
      @click="error = null"
    >{{ error }} <span class="close">✕</span></div>

    <div class="layout">
      <aside>
        <input
          data-testid="user-id-input"
          v-model="userId"
          placeholder="User ID (optional)"
          class="user-input"
          @change="fetchSessions"
        />
        <button
          data-testid="new-session-btn"
          class="btn-primary full-width"
          @click="createSession"
        >+ New Session</button>

        <ul data-testid="session-list" class="session-list">
          <li
            v-for="s in sessions"
            :key="s.id"
            :data-testid="`session-item-${s.session_token}`"
            :class="{ active: activeSession?.id === s.id }"
            @click="selectSession(s)"
          >
            <span class="session-label">#{{ s.id }} <span class="session-user">· {{ s.user_id ?? 'anonymous' }}</span></span>
            <button
              class="del-btn"
              @click.stop="deleteSession(s.id)"
              title="Delete session"
            >✕</button>
          </li>
        </ul>
      </aside>

      <main v-if="activeSession" class="main-content">
        <div class="tabs">
          <button :class="['tab', { active: view === 'chat' }]" @click="view = 'chat'">Chat</button>
          <button :class="['tab', { active: view === 'quiz' }]" @click="view = 'quiz'">Quiz</button>
        </div>

        <!-- Chat view -->
        <div v-if="view === 'chat'" class="chat-view">
          <div data-testid="message-list" class="message-list" ref="messageListEl">
            <p v-if="messages.length === 0" class="empty">No messages yet.</p>
            <div
              v-for="m in messages"
              :key="m.id"
              :data-testid="m.role === 'user' ? 'user-message' : 'assistant-message'"
              :class="['bubble', m.role]"
            >{{ m.content }}</div>
          </div>

          <div v-if="chatLoading" data-testid="chat-loading" class="loading">Thinking…</div>

          <form class="input-row" @submit.prevent="sendMessage">
            <input
              data-testid="message-input"
              v-model="messageText"
              placeholder="Ask something…"
              :disabled="chatLoading"
              autocomplete="off"
            />
            <button
              data-testid="send-message-btn"
              type="submit"
              class="btn-primary"
              :disabled="chatLoading || !messageText.trim()"
            >Send</button>
          </form>
        </div>

        <!-- Quiz view -->
        <div v-else class="quiz-view">
          <div class="quiz-form">
            <input
              data-testid="quiz-topic-input"
              v-model="quizTopic"
              placeholder="Enter a topic to create a quiz."
            />
            <button
              data-testid="generate-quiz-btn"
              class="btn-primary"
              :disabled="quizLoading || !quizTopic.trim()"
              @click="generateQuiz"
            >Generate Quiz</button>
          </div>

          <div v-if="quizLoading" class="loading">Generating…</div>

          <p v-if="quizFeedback" data-testid="quiz-feedback" class="quiz-done">{{ quizFeedback }}</p>
          <div v-if="quizQuestions.length > 0 && !quizFeedback" class="question-box">
            <p class="q-meta">Question {{ currentQIdx + 1 }} / {{ quizQuestions.length }}</p>
            <p data-testid="quiz-question" class="q-text">{{ quizQuestions[currentQIdx] }}</p>

            <div class="options">
              <label v-for="(opt, i) in ['A', 'B', 'C', 'D']" :key="i" class="option-label">
                <input
                  type="radio"
                  :data-testid="`quiz-option-${i}`"
                  :value="opt"
                  v-model="quizAnswer"
                />
                {{ opt }}
              </label>
            </div>

            <button
              data-testid="submit-answer-btn"
              class="btn-primary"
              :disabled="!quizAnswer"
              @click="submitAnswer"
            >Submit Answer</button>

          </div>
        </div>
      </main>

      <main v-else class="placeholder">
        Select a session from the list or create a new one.
      </main>
    </div>
  </div>
</template>

<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: system-ui, sans-serif; background: #f5f5f5; color: #222; height: 100vh; }
#app { height: 100vh; display: flex; flex-direction: column; }
</style>

<style scoped>
.app { display: flex; flex-direction: column; height: 100vh; }

header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 16px;
  height: 52px;
  background: #1a1a2e;
  color: #fff;
  flex-shrink: 0;
}
.logo { font-size: 1.25rem; font-weight: 700; letter-spacing: .05em; }

.badge {
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}
.badge.err      { background: #ef4444; color: #fff; }
.badge.hidden   { visibility: hidden; }

.error-banner {
  background: #fee2e2;
  border-left: 4px solid #ef4444;
  color: #991b1b;
  padding: 8px 16px;
  display: flex;
  justify-content: space-between;
  cursor: pointer;
  flex-shrink: 0;
}
.close { font-size: 0.8rem; opacity: .7; }

.layout { display: flex; flex: 1; overflow: hidden; }

aside {
  width: 220px;
  background: #fff;
  border-right: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 12px;
  flex-shrink: 0;
  overflow-y: auto;
}

.user-input {
  width: 100%;
  padding: 6px 8px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.85rem;
}

.btn-primary {
  background: #1a1a2e;
  color: #fff;
  border: none;
  border-radius: 6px;
  padding: 7px 14px;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
}
.btn-primary:disabled { opacity: .45; cursor: default; }
.btn-primary:hover:not(:disabled) { background: #2d2d4e; }
.full-width { width: 100%; }

.session-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}
.session-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 10px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
  border: 1px solid transparent;
}
.session-list li:hover { background: #f3f4f6; }
.session-list li.active { background: #ede9fe; border-color: #8b5cf6; }
.session-user { color: #8b5cf6; font-size: 0.75rem; }

.del-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: #9ca3af;
  font-size: 0.75rem;
  padding: 2px 4px;
  border-radius: 4px;
  line-height: 1;
}
.del-btn:hover { color: #ef4444; background: #fee2e2; }

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.tabs {
  display: flex;
  border-bottom: 1px solid #e5e7eb;
  background: #fff;
  flex-shrink: 0;
}
.tab {
  padding: 10px 20px;
  border: none;
  background: none;
  cursor: pointer;
  font-size: 0.9rem;
  color: #6b7280;
  border-bottom: 3px solid transparent;
}
.tab.active { color: #1a1a2e; border-bottom-color: #8b5cf6; font-weight: 600; }

/* Chat */
.chat-view {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: #f9fafb;
}
.message-list {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.empty { color: #9ca3af; text-align: center; margin-top: 40px; font-size: 0.9rem; }
.bubble {
  max-width: 70%;
  padding: 10px 14px;
  border-radius: 12px;
  font-size: 0.9rem;
  line-height: 1.5;
  word-break: break-word;
}
.bubble.user { background: #1a1a2e; color: #fff; align-self: flex-end; border-bottom-right-radius: 4px; }
.bubble.assistant { background: #fff; border: 1px solid #e5e7eb; align-self: flex-start; border-bottom-left-radius: 4px; }
.loading { padding: 6px 16px; color: #6b7280; font-size: 0.8rem; font-style: italic; flex-shrink: 0; }
.input-row {
  display: flex;
  gap: 8px;
  padding: 12px;
  background: #fff;
  border-top: 1px solid #e5e7eb;
  flex-shrink: 0;
}
.input-row input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.9rem;
}
.input-row input:focus { outline: none; border-color: #8b5cf6; }

/* Quiz */
.quiz-view {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  background: #f9fafb;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.quiz-form { display: flex; gap: 10px; }
.quiz-form input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  font-size: 0.9rem;
}
.question-box {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.q-meta { font-size: 0.75rem; color: #9ca3af; text-transform: uppercase; letter-spacing: .05em; }
.q-text { font-size: 1rem; font-weight: 600; line-height: 1.5; }
.options { display: flex; flex-direction: column; gap: 8px; }
.option-label {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
}
.option-label:has(input:checked) { border-color: #8b5cf6; background: #ede9fe; }
.quiz-done { margin-top: 10px; color: #059669; font-weight: 600; font-size: 0.9rem; }


/* Placeholder */
.placeholder {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #9ca3af;
  font-size: 0.95rem;
}
</style>

<!--
Tool Used: Claude Sonnet 4.6
Purpose: Used to generate the Vue frontend (structure, logic, styling).
-->

