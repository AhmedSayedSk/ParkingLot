<?php

# contributor: Ahmed Sayed
# ------------------------

$file_name = "reading.txt";

$myfile = @fopen($file_name, "r") or die("unable_to_open_file");

echo @fread($myfile, filesize($file_name));

fclose($myfile);