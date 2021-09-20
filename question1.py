class Hw1Q1:
    def timeConvert(input_second):
         day = input_second // (24 * 3600)
         input_second = input_second % (24 * 3600)
         hour = input_second // 3600
         input_second %= 3600
         minute = input_second // 60
         input_second %= 60
         second = input_second

         if day == 1:
              d = str(day) + " day, "
         elif day > 1:
              d = str(day) + " days, "

         if hour == 1:
             h = str(hour) + " hour, "
         elif hour > 1:
             h = str(hour) + " hours, "

         if minute == 1:
             m = str(minute) + " minute, "
         elif minute > 1:
             m = str(minute) + " minutes, "

         if second == 1:
             s = str(second) + " second "
         elif second > 1:
             s = str(second) +  " seconds "

         output = ""
         output = d + h + m + s
         return output


    input_second = int(input("Enter the seconds: "))
    print(timeConvert(input_second))
