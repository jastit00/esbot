from behave import when, then

# --- Scenario 1: Successful upload ---

@when('the student navigates to "Upload Material"')
def step_impl_1_1(context):
    context.navigated = True

@when("the student selects one or more files")
def step_impl_1_2(context):
    context.selected_files = ["lecture_notes.pdf"]
    context.file_valid = True

@when("the student confirms the upload")
def step_impl_1_3(context):
    context.upload_confirmed = True

@then("the system validates the input")
def step_impl_1_4(context):
    assert context.file_valid is True

@then("the system stores the material in persistent storage")
def step_impl_1_5(context):
    context.storage_success = True

@then("the system links the material to the student context")
def step_impl_1_6(context):
    context.material_linked = True

@then("the student sees a confirmation message")
def step_impl_1_7(context):
    context.confirmation_shown = True

@then('the student is offered next actions like "summarize", "ask questions", or "request test"')
def step_impl_1_8(context):
    context.next_actions = ["summarize", "ask questions", "request test"]

# --- Scenario 2: Invalid or unsupported material ---

@when("the student selects an unsupported file type or oversized file or unreadable content")
def step_impl_2_1(context):
    context.selected_files = ["other.exe"]
    context.file_valid = False

@then("the system detects invalid input")
def step_impl_2_2(context):
    assert context.file_valid is False

@then("the system asks the student to adjust or upload different material")
def step_impl_2_3(context):
    context.adjustment_requested = True

# --- Scenario 3: Storage error ---

@when("the student selects valid material")
def step_impl_3_1(context):
    context.selected_files = ["notes.pdf"]
    context.file_valid = True

@when("the system cannot store the material due to not enough storage being available")
def step_impl_3_2(context):
    context.storage_success = False

@then("the system informs the student that the upload failed")
def step_impl_3_3(context):
    assert context.storage_success is False
    context.error_shown = True

@then("the system suggests retrying later and informing an administrator")
def step_impl_3_4(context):
    context.retry_suggestion = True
