from .elements_page import ElementsPage
from ..locators import ElementsPageLocators


class TextBoxSubTub(ElementsPage):
    def should_be_full_name_field_on_text_box_sub_tub(self):
        assert self.is_element_present(*ElementsPageLocators.TEXT_BOX_SUB_TUB_FULL_NAME_FIELD), \
            "Full name field is missing on Elements page, text box sub-tub"

    def should_be_email_field_on_text_box_sub_tub(self):
        assert self.is_element_present(*ElementsPageLocators.TEXT_BOX_SUB_TUB_EMAIL_FIELD), \
            "Email field is missing on Elements page, text box sub-tub"

    def should_be_current_address_field_on_text_box_sub_tub(self):
        assert self.is_element_present(*ElementsPageLocators.TEXT_BOX_SUB_TUB_CURRENT_ADDRESS_FIELD), \
            "Current address field is missing on Elements page, text box sub-tub"

    def should_be_permanent_address_field_on_text_box_sub_tub(self):
        assert self.is_element_present(*ElementsPageLocators.TEXT_BOX_SUB_TUB_PERMANENT_ADDRESS_FIELD), \
            "Permanent address field is missing on Elements page, text box sub-tub"

    def should_be_text_box_form_on_text_box_sub_tub(self):
        self.should_be_full_name_field_on_text_box_sub_tub()
        self.should_be_email_field_on_text_box_sub_tub()
        self.should_be_current_address_field_on_text_box_sub_tub()
        self.should_be_permanent_address_field_on_text_box_sub_tub()

    def should_be_submit_button_on_text_box_sub_tub(self):
        assert self.is_element_present(*ElementsPageLocators.TEXT_BOX_SUB_TUB_SUBMIT_BUTTON), \
            "Submit button is missing on Elements page, text box sub-tub"
