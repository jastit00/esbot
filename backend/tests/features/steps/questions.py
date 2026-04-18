from behave import given, when, then, step

# Global-like state via context (Requirement: test data in lifecycle)
def setup_context(context):
    if not hasattr(context, 'esbot_running'):
        context.esbot_running = False
        context.material_uploaded = False
        context.retrieval_success = True
        context.ai_response_type = "clear"
        context.failures = 0

# --- Scenario 1: Successful question answering ---

@given('the student has access to the running EsBot')
def step_impl_1_1(context):
    setup_context(context)
    context.esbot_running = True

@given('the student has previously uploaded at least one material')
def step_impl_1_2(context):
    setup_context(context)
    context.material_uploaded = True

@when('the student submits a question about the material')
def step_impl_1_3(context):
    context.question = "What is the main idea of the document?"
  

@then('the system receives the question with the current context')
def step_impl_1_4(context):
    assert hasattr(context, 'question')

@then('the system determines the relevant material')
def step_impl_1_5(context):

    relevant_materials = [m for m in ["material_1", "material_2"] if context.material_uploaded]
    assert len(relevant_materials) > 0

@then('the system retrieves the relevant content from storage')
def step_impl_1_6(context):
    assert context.retrieval_success is True

@then('the system constructs an AI prompt with question and context')
def step_impl_1_7(context):
    context.ai_prompt ="Question: {context.question}"

@then('the system sends the prompt to the AI engine')
def step_impl_1_8(context):
    context.prompt_sent = True

@then('the system receives an answer')
def step_impl_1_9(context):
 
    context.answer = "This is the AI answer based on the material."
    assert hasattr(context, 'answer')

@then('the system validates and structures the answer')
def step_impl_1_10(context):
    context.validated_answer = context.answer

@then('the system stores the question and answer in session history')
def step_impl_1_11(context):
    # Simulation der Speicherung
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

@given('the student has access to the running EsBot (Scenario 2)')
def step_impl_2_1(context):
    setup_context(context)
    context.esbot_running = True

@given('the student has previously uploaded at least one material (Scenario 2)')
def step_impl_2_2(context):
    setup_context(context)
    context.material_uploaded = True

@then('the system receives the question with the current context (Scenario 2)')
def step_impl_2_3(context):
    context.question = "What is the main idea?"

@then('the system identifies the relevant material')
def step_impl_2_4(context):
    
    relevant_materials = [m for m in ["material_1", "material_2"] if context.material_uploaded]
    assert len(relevant_materials) > 0

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

@given('the student has access to the running EsBot (Scenario 3)')
def step_impl_3_1(context):
    setup_context(context)
    context.esbot_running = True

@given('the student has previously uploaded at least one material (Scenario 3)')
def step_impl_3_2(context):
    setup_context(context)
    context.material_uploaded = True

@when('the student submits a question about the material (Scenario 3)')
def step_impl_3_3(context):
    context.question = "What is the main idea?"

@then('the system receives the question with the current context (Scenario 3)')
def step_impl_3_4(context):
    assert hasattr(context, 'question')

@then('the system identifies the relevant material (Scenario 3)')
def step_impl_3_5(context):
   
    relevant_materials = [m for m in ["material_1", "material_2"] if context.material_uploaded]
    assert len(relevant_materials) > 0


@then('the system retrieves the relevant content from storage (Scenario 3)')
def step_impl_3_6(context):
    context.retrieved_content = "Content for off-topic simulation."

@then('the system constructs an AI prompt with question and context (Scenario 3)')
def step_impl_3_7(context):
    context.ai_prompt = "Question: context.question"

@then('the system sends the prompt to the AI engine (Scenario 3)')
def step_impl_3_8(context):
    context.prompt_sent = True

@when('the system receives an answer from the AI engine')
def step_impl_3_9(context):
    context.answer = "Off-topic answer"

@when('the answer is detected as off-topic or unusable')
def step_impl_3_10(context):
    context.validated_answer = False

@then('the system retries once with an improved prompt')
def step_impl_3_11(context):
    context.retry_attempted = True
    context.improved_prompt = True

@when('the system fails with the improved prompt')
def step_impl_3_12(context):
    if not hasattr(context, 'failures'):
        context.failures = 0
    context.failures += 1

@then('the system informs the student that no suitable explanation can be generated')
def step_impl_3_13(context):
    context.final_error = "No suitable explanation could be generated."
