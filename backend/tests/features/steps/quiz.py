from behave import when, then

# --- Scenario 1: Successful test generation ---

@when("the student requests a test for selected material")
def step_impl_1_3(context):
    context.request_test = True

@then("the system retrieves the material from storage")
def step_impl_1_6(context):
    assert context.retrieval_success is True

@then("the system constructs a prompt for question generation")
def step_impl_1_7(context):
    context.ai_prompt = "Generate quiz questions based on the material."

@then("the system receives a list of questions")
def step_impl_1_9(context):
    context.questions = context.quiz_service.generate("selected material")
    assert hasattr(context, "questions") and len(context.questions) > 0

@then("the system validates and structures the quiz")
def step_impl_1_10(context):
    context.validated_quiz = context.questions

@then("the system stores the quiz in the student session")
def step_impl_1_11(context):
    context.quiz_stored = True

@then("the system presents the quiz to the student")
def step_impl_1_12(context):
    context.quiz_presented = True

# --- Scenario 2: No suitable material selected ---

@when("the system cannot determine relevant material")
def step_impl_2_4(context):
    context.relevant_materials_found = False
    assert context.relevant_materials_found is False

@then("the system asks the student to choose from available materials")
def step_impl_2_5(context):
    context.choose_material = True
    context.question = "Please select the material"

# --- Scenario 3: Material not suitable for test generation ---

@when("the material is too short or too long or unsuitable")
def step_impl_3_6(context):
    context.material_suitable = False

@then("the system suggests alternative material or reduced scope")
def step_impl_3_8(context):
    context.suggest_alternative = True
    context.suggestion = "Please select a different material or change the scope of the content."
