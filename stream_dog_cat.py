import streamlit as st

def main():
    # Заголовок приложения
    st.title("Классификация")

    # Навигационное меню
    menu = ["Главная", "Классификация ImageNet", "Классификация моделью ResNet18 Cats&Dogs", "Классификация клеток крови"]
    choice = st.sidebar.selectbox("Выберите страницу", menu)

    if choice == "Главная":
        show_homepage()
    elif choice == "Классификация ImageNet":
        show_page1()
    elif choice == "Классификация моделью ResNet18 Cats&Dogs":
        show_page2()
    elif choice == "Классификация клеток крови":
        show_page3()

def show_homepage():
    st.header("Добро пожаловать ")
    # Здесь вы можете добавить любой контент для главной страницы
    # Добавляем картинку
    st.image("/Users/cobalt/Desktop/blood.png", use_column_width=True)
def show_page1():
    st.header("Классификация ImageNet")
    # Здесь вы можете добавить любой контент для страницы 1

def show_page2():
    st.header("Классификация моделью ResNet18 Cats&Dogs")
    # Здесь вы можете добавить любой контент для страницы 2

def show_page3():
    st.header("Классификация клеток крови")
    # Здесь вы можете добавить любой контент для страницы 3

if __name__ == '__main__':
    main()
