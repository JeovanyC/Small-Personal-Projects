import sys

bit_map = '''

....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................

'''

def apolizage(w_in_w):
    if w_in_w == "":
        return ("Well... then... let's begin!",)
    else:
        return ("Thank you very much!",)


def main():
    print ('''

Hello! Want to see the evil deed that I can do?

I can transform the entire world into words!
I just need a little help from you...

My creativite is not quite good today, can you give me an idea of a world to use?
''')

    w_in_w = input("> ")
    answer = apolizage(w_in_w)
         
    if w_in_w == "":
        print('''

You!... You tried to fool me!...

I just wanted some help... and you toyed with me...
Don't you feel any shame in that?...

(Do you want to apolizage? [yes or no])
''')

        if not input("> ").lower().startswith("y"):
            sys.exit()
            print("Well... Farewell then!")
        else:
            print('''
I'm willing to give you one last chance...

(type something to help the evil deed be completed)
''')
            w_in_w = input("> ")
            if w_in_w == "":
                print('''
Serius? Again trying this same old trick?...
                
Wanna now something? I'm not showing you anything!
''')
                sys.exit()



    if w_in_w != "":
        print('''
        
{}

Now!
Wait and see!

HAHAHAHAHAH!

The world in words!

HAHAHAHAHA! *cough *cough

'''.format(answer[0]))
        for line in bit_map.splitlines():
            for i, bit in enumerate(line):
                if bit == " ":
                    print(" ", end = "")
                else:
                    print(w_in_w[(i % len(w_in_w))], end = "")
            print ()


if __name__ == "__main__":
    main()