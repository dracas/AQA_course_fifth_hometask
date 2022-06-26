from selenium.webdriver.common.by import By


class BasepageLocators:
    ELEMENTS_PAGE = (By.CSS_SELECTOR, ".category-cards:first-child .card-body :first-child")
    FORMS_PAGE = (By.CSS_SELECTOR, ".category-cards:first-child .card-body :first-child")


class ElementsPageLocators:
    # welcome text
    WELCOME_TEXT = (By.CSS_SELECTOR, ".row .col-md-6")
    # text-box sub-tub
    TEXT_BOX_SUB_TUB = (By.CSS_SELECTOR, ".left-pannel .accordion :nth-child(1) .element-list #item-0")
    TEXT_BOX_SUB_TUB_FULL_NAME_FIELD = (By.CSS_SELECTOR, "#userName-wrapper .mr-sm-2")
    TEXT_BOX_SUB_TUB_EMAIL_FIELD = (By.CSS_SELECTOR, "#userEmail-wrapper .mr-sm-2")
    TEXT_BOX_SUB_TUB_CURRENT_ADDRESS_FIELD = (By.CSS_SELECTOR, "#currentAddress")
    TEXT_BOX_SUB_TUB_PERMANENT_ADDRESS_FIELD = (By.CSS_SELECTOR, "#permanentAddress")
    TEXT_BOX_SUB_TUB_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    # check-box sub-tub
    CHECK_BOX_SUB_TUB = (By.CSS_SELECTOR, ".left-pannel .accordion :nth-child(1) .element-list #item-1")
    # radio button sub-tub
    RADIO_BUTTON_SUB_TUB = (By.CSS_SELECTOR, ".left-pannel .accordion :nth-child(1) .element-list #item-2")
    RADIO_BUTTON_SUB_TUB_YES_BTN = (By.CSS_SELECTOR, '.custom-control-label[for="yesRadio"]')
    RADIO_BUTTON_SUB_TUB_IMPRESSIVE_BTN = (By.CSS_SELECTOR, '.custom-control-label[for="impressiveRadio"]')
    RADIO_BUTTON_SUB_TUB_NO_BTN = (By.CSS_SELECTOR, '.custom-control-label[for="noRadio"]')
    RADIO_BUTTON_SUB_TUB_MESSAGE = (By.CSS_SELECTOR, '.mt-3')
    # buttons sub-tub
    BUTTONS_SUB_TUB = (By.CSS_SELECTOR, ".left-pannel .accordion :nth-child(1) .element-list #item-4")
    BUTTONS_SUB_TUB_DOUBLE_CLICK_BTN = (By.CSS_SELECTOR, "#doubleClickBtn")
    BUTTONS_SUB_TUB_RIGHT_CLICK_BTN = (By.CSS_SELECTOR, "##rightClickBtn")
    BUTTONS_SUB_TUB_CLICK_BTN = (By.CSS_SELECTOR, ".col-md-6 :nth-child(3) button")
    BUTTONS_SUB_TUB_DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, "#doubleClickMessage")
    BUTTONS_SUB_TUB_RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, "#rightClickMessage")
    BUTTONS_SUB_TUB_DYNAMIC_CLICK_MESSAGE = (By.CSS_SELECTOR, "#dynamicClickMessage")


class FormsPageLocators:
    pass
