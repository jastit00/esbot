from behave import given, when, then, step

# Global-like state via context (Requirement: test data in lifecycle)
def setup_context(context):
    if not hasattr(context, "esbot_running"):
        context.esbot_running = False
        context.material_uploaded = False
        context.retrieval_success = True
        context.ai_response_type = "clear"
        context.failures = 0

# --- Scenario 1: Successful question answering ---

@given("the student has access to the running EsBot")
def step_impl_1_1(context):
    setup_context(context)
    context.esbot_running = True

@given("the student has previously uploaded at least one material")
def step_impl_1_2(context):
    setup_context(context)
    context.material_uploaded = True

@when("the student requests a test for selected material")
def step_impl_1_3(context):
    context.request_test = True

@then("the system determines the relevant material")
def step_impl_1_4(context):
    # Simulate filtering for relevant materials
    relevant_materials = [m for m in ["material_1", "material_2"] if context.material_uploaded]
    assert len(relevant_materials) > 0

@then("the system evaluates the selected material")
def step_impl_1_5(context):
    context.evaluation_result = "Material is suitable for quiz generation."

@then("the system retrieves the material from storage")
def step_impl_1_6(context):
    assert context.retrieval_success is True

@then("the system constructs a prompt for question generation")
def step_impl_1_7(context):
    context.ai_prompt = "Generate quiz questions based on the material."

@then("the system sends the prompt to the AI engine")
def step_impl_1_8(context):
    context.prompt_sent = True  

@then("the system receives a list of questions")
def step_impl_1_9(context):
    context.questions = ["What is the main idea of the document?", "List three key points from the material."]
    assert hasattr(context, "questions")

@then("the system validates and structures the quiz")
def step_impl_1_10(context):
    context.validated_quiz = context.questions

@then("the system stores the quiz in the student session")
def step_impl_1_11(context):
    # Simulation: Store in session
    context.quiz_stored = True

@then("the system presents the quiz to the student")
def step_impl_1_12(context):
    context.quiz_presented = True

    
 # Scenario 2: No suitable material selected

@given("the student has access to the running EsBot (Scenario 2)")
def step_impl_2_1(context):
    setup_context(context)
    context.esbot_running = True

@given("the student has previously uploaded at least one material (Scenario 2)")
def step_impl_2_2(context):
    setup_context(context)
    context.material_uploaded = True

@when("the student requests a test for selected material (Scenario 2)")
def step_impl_2_3(context):
    context.request_test = True

@when("the system cannot determine relevant material")
def step_impl_2_4(context):
    # Force failure for this scenario
    context.relevant_materials_found = False
    assert context.relevant_materials_found is False

@then("the system asks the student to choose from available materials")
def step_impl_2_5(context):
    context.choose_material = True
    context.question = "Please select the material"


#Scenario 3: Material not suitable for test generation

@given("the student has access to the running EsBot (Scenario 3)")
def step_impl_3_1(context):
    setup_context(context)
    context.esbot_running = True

@given("the student has previously uploaded at least one material (Scenario 3)")
def step_impl_3_2(context):
    setup_context(context)
    context.material_uploaded = True    

@when("the student requests a test for selected material (Scenario 3)")
def step_impl_3_3(context):
    context.request_test = True 
 
@then("the system determines the relevant material (Scenario 3)")
def step_impl_3_4(context):
    relevant_materials = [m for m in ["material_1", "material_2"] if context.material_uploaded]
    assert len(relevant_materials) > 0

@when("the system evaluates the selected material (Scenario 3)")
def step_impl_3_5(context):
    context.evaluation_started = True

@when("the material is too short or too long or unsuitable")
def step_impl_3_6(context):
    context.material_suitable = False
    
@then("the system informs the student about the issue")
def step_impl_3_7(context):
    assert context.material_suitable is False
    context.inform_student = True
    context.message = "The selected material is not suitable for quiz generation."
 
@then("the system suggests alternative material or reduced scope")
def step_impl_3_8(context):
    context.suggest_alternative = True
    context.suggestion = "Please select a different material or change the scope of the content."
