import time


def test_button_add_to_basket_should_be_present(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Небольшая пауза для визуальной проверки языка
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину по уникальному селектору
    button = browser.find_element(
        "css selector",
        "button.btn-add-to-basket"
    )
    
    # Проверяем, что кнопка найдена и отображается
    assert button is not None, "Кнопка добавления в корзину не найдена"
    assert button.is_displayed(), "Кнопка добавления в корзину не отображается"