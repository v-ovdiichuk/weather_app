import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=uk"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"Температура: {temp}°C\nОпис: {description}"
    else:
        return "Помилка отримання даних про погоду"
    
class WeatherApp (ctk.CTk):
        def __init__(self):
            super().__init__()

            self.title("Weather App")
            self.geometry("400x300")

            self.label = ctk.CTkLabel(self, text="Введи місто:")
            self.label.pack(pady=10)

            self.entry = ctk.CTkEntry(self)
            self.entry.pack(pady=10)

            self.button = ctk.CTkButton(self, text="Отримати погоду", command=self.show_weather)
            self.button.pack(pady=10)

            self.result_label = ctk.CTkLabel(self, text="")
            self.result_label.pack(pady=10)

            self.api_key ="e0caa1ee69ae0871544acc1ede27ea60"

        def show_weather(self):
            city = self.entry.get()
            if city:
                result = get_weather(city, self.api_key)
                self.result_label.configure(text=result)
            else:
                self.result_label.configure(text="Введи місто!")

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()