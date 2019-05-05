# contributor: Ahmed Sayed Ahmed
# -------------------------------

def export_reading_in_file(array):
    if(len(array)):
        seperator = ','
        text_file = open("app/reading.txt", "w")
        text_file.write(','.join([str(i) for i in array]))
        text_file.close()