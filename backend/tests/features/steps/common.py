from behave import given, step


def setup_context(context):
    if not hasattr(context, "esbot_running"):
        context.esbot_running = False
        context.material_uploaded = False
        context.retrieval_success = True
        context.ai_response_type = "clear"
        context.failures = 0


@given("the student has access to the running EsBot")
def step_esbot_running(context):
    setup_context(context)
    context.esbot_running = True


@given("the student has previously uploaded at least one material")
def step_material_uploaded(context):
    setup_context(context)
    context.material_uploaded = True


@step("the system determines the relevant material")
def step_determines_material(context):
    relevant_materials = [m for m in ["material_1", "material_2"] if context.material_uploaded]
    assert len(relevant_materials) > 0


@step("the system sends the prompt to the AI engine")
def step_sends_prompt(context):
    context.prompt_sent = True


@step("the system evaluates the selected material")
def step_evaluates_material(context):
    context.evaluation_started = True
    context.evaluation_result = "Material is suitable for quiz generation."


@step("the system informs the student about the issue")
def step_informs_issue(context):
    context.inform_student = True
