from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class ChatBotApp(App):
    def build(self):
        self.window = BoxLayout(orientation="vertical")
        self.chat_history = Label(
            size_hint=(1, 0.8),
            text="ChatBot : မင်္ဂလာပါ ။ Tech abbreviations you need to know",
            font_name="font.ttf",
            halign="left",
            valign="top",
        )

        self.window.add_widget(self.chat_history)

        self.user_input = TextInput(
            size_hint=(1, 0.1), font_name="font.ttf", multiline=False
        )
        self.window.add_widget(self.user_input)

        self.send_button = Button(text="send", size_hint=(1, 0.1))

        self.send_button.bind(on_release=self.send_message)

        self.window.add_widget((self.send_button))

        return self.window

    def send_message(self, instance):
        user_message = self.user_message = self.user_input.text
        if user_message:
            bot_response = self.get_bot_response(user_message)
            new_text = f"\n\nYou: {user_message}\nChatBot: {bot_response}"
            self.chat_history.text += new_text
            self.user_input.text = ""

    def get_bot_response(self, message):
        # အလွန်ရိုးရှင်းသော Logic များ
        if "Hello" in message:
            return "Hello ! Nice to meet you  "
        elif "ဟယ်လို" in message:
            return "ဟယ်လို မင်္ဂလာပါ"
        elif "နေကောင်းလား?" in message:
            return "ကျန်းမာပါတယ်ဗျာ သင်ရော နေကောင်းပါသလား?"
        elif "ဘာလုပ်နေလဲ?" in message:
            return "သင်မေးတာတွေဖြေနေပါတယ်... ဖြေနိုင်သည်များကိုသာမေးပါ :( "
        elif "ဟိုင်း" in message:
            return "ဟိုင်း နေကောင်းလား"
        elif "Hi" in message:
            return "Hi How are you?"
        elif "Who are you?" in message:
            return "I am Bot ... Chat Bot :P "
        elif "မျိုးကျော်သူ" in message:
            return "ဖန်တီးထားသူပါ"
        elif "ဆူးငယ်သစ်" in message:
            return "ဆူးငယ်သစ်(ရန်ကုန်)ပါ မျိုးကျော်သူပါဘဲ"
        elif "ဇွဲထက်ထွဋ်" in message:
            return "အရမ်းချောတယ်တယ်"
        elif "What is your name? " in message:
            return "I am Chat Bot"
        elif "မင်းနာမည်ဘယ်လိုခေါ်လဲ?" in message:
            return "ကျနော် နာမည် ချက်ဘော့ထ် ပါ"
        elif "မင်္ဂလာပါ" in message:
            return "မင်္ဂလာပါ ဘာတွေမေးလို့ရလဲဆိုတာ သိဖို့ ကူညီပါ သို့မဟုတ် Help ဟု ရိုက်ပါ :P "
        elif "Who is create you?" in message:
            return "My creator is U Myo Kyaw Thu"
        elif "မင်းကိုဘယ်သူဖန်တီးထားတာလဲ?" in message:
            return "ကျနော်ကို ဦးမျိုးကျော်သူမှ ဖန်တီးထားပါတယ်။"
        elif "Help" in message:
            return "Your Type is RAN, GPS,ROM, SMS,CPU,COMPUTER,OTP,WI-FI"
        elif "help" in message:
            return "Your Type is RAN, GPS,ROM, SMS,CPU,COMPUTER,OTP,WI-FI"
        elif "ကူညီပါ" in message:
            return "RAM, GPS,ROM, SMS,CPU,COMPUTER,OTP,WI-FI များကို ရိုက်ရှာနိုင်ပါသည်။"
        elif "WI-FI" in message:
            return "Wireless Fidelity"
        elif "ROM" in message:
            return "Read-Only Memory"
        elif "RAM" in message:
            return "Random Access Memory"
        elif "Wi-Fi" in message:
            return "Wireless Fidelity"
        elif "wifi" in message:
            return "Wireless Fidelity"
        # elif "clean" in message:
        #     return
        elif "OTP" in message:
            return "One-Time Password"
        elif "otp" in message:
            return "One-Time Password"
        elif "COMPUTER" in message:
            return "Common Operation Machine Particularly Used for Technical, Educational, and Research"
        elif "computer" in message:
            return "Common Operation Machine Particularly Used for Technical, Educational, and Research"
        elif "CPU" in message:
            return "Central Processing Unit"
        elif "cpu" in message:
            return "Central Processing Unit"
        elif "SMS" in message:
            return "Short Message Service"
        elif "sms" in message:
            return "Short Message Service"
        elif "GPS" in message:
            return "Global Positioning System"

        else:
            return "စမ်းသပ်စဲ ကာလဖြစ်ပါတယ်...မေးလို့ ရသည်များကိုသာ ဖြေကြားပေးပါတယ် ခင်ဗျာ....Help သို့မဟုတ် ကူညီပါ ဟုရိုက်ပါ"


if __name__ == "__main__":
    ChatBotApp().run()
