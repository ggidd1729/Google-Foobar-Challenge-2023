# this program decodes data to ASCII text. The first argument specifies the
# base of the encoded data. The program then receives the encoded data
# through space delimited arguments

for ((i = 2; i <= $#; i++ )); do
  octal=$(echo 'obase=8; ibase='$1'; '${!i}'' | bc)
  printf "\\$octal"
done
