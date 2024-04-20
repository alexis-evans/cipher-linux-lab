import sys

# message = "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the government for a redress of grievances"
shift = int(sys.argv[1])
message = ""
for line in sys.stdin:
  if 'q' == line.rstrip():
    break
  message += line


message = ''.join([char for char in message if char.isalpha()])
message = message.upper()

#cipher time
cipher = ""
for index in range(len(message)):
  char = message[index]
  ascii_code = ord(char)
  if ascii_code + shift > 90: 
    # new = original + whatever gets you to 90 - 26 + remainder
    gets_you_to_90 = 90 - ascii_code
    remainder = shift - gets_you_to_90
    new_char = chr(ascii_code + gets_you_to_90 - 26 + remainder)
  else: 
    new_char = chr(ascii_code + shift)
  cipher += new_char


#printing message
current_block_length = 0
blocks_in_line = 0
final_message = ""
#index of chars after spaces: index % 5 == 0
#index of chars after new lines: index % 50 == 0

for index in range(len(cipher)):
  if index % 50 == 0:
    final_message += "\n" + cipher[index]
  elif index % 5 == 0:
    final_message += " " + cipher[index]
  else:
    final_message += cipher[index]

print(final_message)






