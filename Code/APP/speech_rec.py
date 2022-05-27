import speech_recognition as sr

class speech_rec:
    #variable to wait till orders has been done
    def __init__(self):
        self.order = False
        #drinks options, values will be direction of drink and if its alcohol or not
        self.drinks = {"ron":True, "ginebra":True, "fanta":True, "cola":True}


    def get_order(self,audio_data,aviable_drinks):
        order = []
        text = audio_data.lower()
        drink_keys = aviable_drinks.keys()
        for word in text.split(" "):
            if word in drink_keys:
                order.append(word)
        return order

    def get_audio_data(self):
        while not self.order:
            r = sr.Recognizer()
            with sr.Microphone() as mic:
                print("Say something!")
                r.adjust_for_ambient_noise(mic, duration=0.2)
                audio = r.listen(mic)

            # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                audio_data = r.recognize_google(audio, language = "es-ES")
                self.order = self.get_order(audio_data,self.drinks)
                print("Google Speech Recognition thinks you said in Spanish: -  " + audio_data)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return self.order