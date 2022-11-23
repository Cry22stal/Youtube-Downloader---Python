# This code is made by Shubhankar Anuragi.

# final edit: 03:12 AM
# exeption handling, colored texts, loading..., sundarta

# maut aajaye magar insomnia ka ilaaj karwa jaaye

# Download happens here:
def Download():
    qual=int(input("Please enter the item number."))
    itag=str(tyype[qual]).split()[1]
    print(itag[6:-1])
    final= found.streams.get_by_itag(itag[6:-1])
    print("\033[1;32mDownload Started!...\033[0m")                #\033[1;32m TEXT \033[0m  : Green Color
    print("Your File is saved at:" + final.download(f"./{x}"))
    filename=str(final.download(f"./{x}")).split("\\")[-1]        # FUCK i am a fucking genius
    print("\033[1;32mDownload Completed! \033[0m")                #\033[1;32m TEXT \033[0m  : Green Color
    print("Thanks For using my YouTube Downloader :)")

# Name Change happens here:
    if flagg==1:
        if "mp3" not in filename:                                      #big brain move
            print("I detected that the file is in not in mp3 format. Would you like me to transform the file to .mp3 format?")
            a=input("Yes/No")
            if a=="Yes" or a=="yes":
                import os
                oldfile_plus_path = os.path.join(f"./{x}", filename)        #FUCKUPS!! DIMAAG LAGANA PADEGA BAHOT
                newfile = filename.split('.')[0]
                newfile_plus_path= os.path.join(f"./{x}", newfile)
                try:                                                                            # My genius sometimes frightens me
                    os.rename(f"{oldfile_plus_path}", f"{newfile_plus_path}.mp3")
                except (FileNotFoundError, FileExistsError) as fileerror:
                    print("\033[91mFile Renaming Error.\033[0m")
                else:
                    print("Changed the extension of the file successfully.")
                finally:
                    print("Thanks For using my YouTube Downloader :)")
            elif a=="No" or a=="no":
                print("Aye Aye Captain!")
                print("Thanks For using my YouTube Downloader :)")
            else:
                print("I will consider this as a no :)")
                print("Thanks For using my YouTube Downloader :)")

# 36 lines ka function, well done shubhankar -,- xDD anything to make it work <3


# Main Code fuckup:
from pytube import YouTube
print("Welcome To Youtube Downloader")
print("\033[1;32mThis Program is made by Shubhankar Anuragi. \033[0m")      #"\033[1;32m GREEN LUND \033[0m"
# link="https://youtu.be/9Za8ZtfHXXY"
try:
    link=input("Paste the link to be downloaded \n")
    found= YouTube(link)
except (Exception) as excep:                                            # galat link ka error handle hojayega ezpz
    print("\033[91mPlease Enter a valid Link.\033[0m")                  # "\033[91m  RED LUND" \033[0m"
else:
    audvid=int(input("What do you want? Please choose the item number. \n 1.Audio Only \n 2.Audio+Video \n"))




# ONLY AUDIO KE LIYE:
    import time
    a = "\033[93mLOADING\033[0m"  # "\033[93m Yellow LUND \033[0m"
    b = "\033[93m.\033[0m"  # "\033[93m Yellow LUND \033[0m"
    if audvid==1:                                   # 1 stands for audio only
        x="Audio"
        print("Please Select Download Quality:\n")
        tatti="taazi"
        i=0
        import time
        a = "\033[93mLOADING\033[0m"  # "\033[93m Yellow LUND \033[0m"
        b = "\033[93m.\033[0m"  # "\033[93m Yellow LUND \033[0m"
        while tatti=="taazi":
            if i<5:
                print(a+(b*i), end="\r")
                i+=1
                time.sleep(1.3)
            elif i==5:
                tatti="baasi"
        if found.streams.filter(progressive=False):        #progressive false matlab gandi quality video + MOSTLY Audios
            tyype = found.streams.filter(type="audio")     # because bahot saare videos bhi aare hain
            for i, v in enumerate(tyype):
                format=str(v).split()[4]
                quality=str(v).split()[3]
                print(f"{i}. {format[8:-1]}" + f" - {quality[5:-1]}")
        flagg=1
        Download()                                       #calling download fn

# AUDIO + VIDEO KE LIYE:
    elif audvid==2:                                 # 2 stands for audio+video
        x="Video"
        print("Please Select Download Quality:\n")
        tatti = "taazi"
        i = 0
        import time
        a = "\033[93mLOADING\033[0m"  # "\033[93m Yellow LUND \033[0m"
        b = "\033[93m.\033[0m"  # "\033[93m Yellow LUND \033[0m"
        while tatti == "taazi":
            if i < 5:
                print(a + (b * i), end="\r")
                i += 1
                time.sleep(1.3)
            elif i == 5:
                tatti = "baasi"
        tyype=found.streams.filter(progressive=True)        #progressive true matlab video
        for i, v in enumerate(tyype):
            format=str(v).split()[2]                                # v easy peasy simple logic defined here, used neeche
            res=str(v).split()[3]                                   # resolution same
            fps=str(v).split()[4]                                   # same
            print(f"{i}. {format[17:-1]}" + f" - {res[5:-1]}" + f" - {fps[5:-1]}")  #used yaha pe, just to make it look sundar
        flagg=0
        Download()              # function defined upar taaki kam mehnat karu hehe
    else:
        print("Please Select a Valid Option, dumbfuck :)")