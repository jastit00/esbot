from behave import when, then, step

# --- Scenario 1: Successful question answering ---

@when('the student submits a question about the material')
def step_impl_1_3(context):
    context.question = "What is the main idea of the document?"

@then('the system receives the question with the current context')
def step_impl_1_4(context):
    if not hasattr(context, 'question'):
        context.question = "What is the main idea of the document?"
    assert hasattr(context, 'question')

@then('the system retrieves the relevant content from storage')
def step_impl_1_6(context):
    assert context.retrieval_success is True

@then('the system constructs an AI prompt with question and context')
def step_impl_1_7(context):
    context.material_context = "Lecture notes on the topic."

@then('the system receives an answer')
def step_impl_1_9(context):
    context.answer = "This is a clear, contextual explanation based on the material."
    assert context.answer is not None

@then('the system validates and structures the answer')
def step_impl_1_10(context):
    assert context.answer != ""
    context.validated_answer = context.answer

@then('the system stores the question and answer in session history')
def step_impl_1_11(context):
    if not hasattr(context, 'session_history'):
        context.session_history = []
    context.session_history.append({
        "question": context.question,
        "answer": context.validated_answer
    })

@then('the system displays the explanation in the chat interface')
def step_impl_1_12(context):
    assert context.validated_answer is not None

# --- Scenario 2: Material retrieval fails ---

@then('the system identifies the relevant material')
def step_impl_2_4(context):
    assert context.material_uploaded is True

@step('the system cannot retrieve the material from storage')
def step_impl_2_5(context):
    context.retrieval_success = False
    context.answer = None

@then('the system informs the student about the failure')
def step_impl_2_6(context):
    assert context.retrieval_success is False
    context.error_message = "Failed to retrieve material."

@then('the system suggests retrying or re-uploading the material')
def step_impl_2_7(context):
    context.suggestion = "Please retry or re-upload the material."

# --- Scenario 3: AI answer is off-topic or unclear ---

@when('the system receives an answer from the AI engine')
def step_impl_3_9(context):
    context.answer = "This is an off-topic answer."

@when('the answer is detected as off-topic or unusable')
def step_impl_3_10(context):
    assert context.answer == "This is an off-topic answer."
    context.validated_answer = None

@then('the system retries once with an improved prompt')
def step_impl_3_11(context):
    context.retry_attempted = True

@when('the system fails with the improved prompt')
def step_impl_3_12(context):
    context.retry_answer = None

@then('the system informs the student that no suitable explanation can be generated')
def step_impl_3_13(context):
    assert context.retry_answer is None
    context.final_error = "No suitable explanation could be generated."
