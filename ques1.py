import speech_recognition as sr
while True:
    with sr.Microphone() as source:
        print("SAY SOMETHING");
        audio = r.listen(source)
        print("TIME OVER, THANKS")


    try:
        s2t=r.recognize_google(audio)
        print("TEXT: "+s2t);
        f=open("C://Users//Lenovo//Desktop//IPY//SpeechToText//STT.txt", "a");       
        f.write(s2t);
        f.close();
        print("FILE ENTRY MADE");

    except:
        pass;
