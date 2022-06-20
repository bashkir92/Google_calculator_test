from Pages.GooglePage import Search

def test_google_calculator(browser):
    google = Search(browser)
    google.go_to_site()
    google.enter_word('Калькулятор')
    google.click_on_the_search_button()
    google.click_on_one()
    google.calculate('mult')
    google.click_on_two()
    google.calculate('minus')
    google.click_on_three()
    google.calculate('plus')
    google.click_on_one()
    google.click_on_equals()
    assert google.line_memory() == '1 × 2 - 3 + 1 ='
    assert google.line_result() == '0'


