import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
import torchvision.models as models
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load('resnet18_full_model.pth', map_location=device)
model.eval()

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
    st.image("blood.png", use_column_width=True)
def show_page1():
    st.header("Классификация ImageNet")
    # Здесь вы можете добавить любой контент для страницы 1
def predict(image):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(image)
        predicted = (torch.sigmoid(output) > 0.5).float().item()
    return "Псина обнаружена" if predicted else "Это котик!"

def show_page2():
    
    st.header("Классификация моделью ResNet18 Cats&Dogs")
    # Здесь вы можете добавить любой контент для страницы 2
    
    uploaded_file = st.file_uploader("Загрузите картинку", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        label = predict(image)
        st.write(f'The uploaded image most likely belongs to a {label}.')

def show_page3():
    st.header("Классификация клеток крови")
    # Здесь вы можете добавить любой контент для страницы 3

if __name__ == '__main__':
    main()
