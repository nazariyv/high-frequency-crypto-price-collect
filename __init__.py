from chuck import ChuckNorris

chucky = ["                                    MMMMMMMMMMM                                         ",
          "                                 MMMMMMMMMMMMMMMMM                                      ",
          "                             NMMMMMMMMMMMMMMMMMMMMMMMM                                  ",
          "                           MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                              ",
          "                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN                          ",
          "                          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                         ",
          "                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                        ",
          "                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD                       ",
          "                        DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                       ",
          "                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                       ",
          "                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                       ",
          "                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                      ",
          "                       MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                      ",
          "                      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN                     ",
          "                      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN         ",
          "                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN     ",
          "                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN   ",
          "NM                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  ",
          "MMMMM              MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM ",
          " MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
          "  MMMMMMMMMMMMMMMMMMMMMMMMMM8MMMMMMMMMIMMMMM8,. ...........OMMMMMMMMMMMMMMMMMMMMMMMMMMMM",
          "     MMMMMMMMMMMMMMMMMMMMMMM ..N. .....~MMMM...............:MMMMNMMMMMMMMMMMMMMMMMMMMMMM",
          "       NMMMMMMMMMMMMMMMMMMMMM.....:..DMMMMMNZ Z.... .......M$MMMMMMMMMMMMMMMMMMMMMMMMMMM",
          "           MMMMMMMMMMNMMMMMMM....... 7=MMMMMMO....Z .......MM7MMMMMMMMMMMMMMMMMMMMMMMMM ",
          "              MMMMMMMMMMMMMMMMM  Z...MMMZ .. .,M..,........MMMMMMMMMMMMMMMMMMMMMMMMMMMM ",
          "                  MMMMMM.......DOM ....N7..................MMMMMMMMMMMMMMMMMMMMMMMMMMM  ",
          "                     MMM....... M. ... .  ... ..............M...$MMMMMMMMMMMMMMMMMMMM   ",
          "                       ........... ........~. ..............M..=....+MMMMMMMMMMMMMM     ",
          "                       ......+.NMI~........ . ..............M.,.I...MMMMMMMMMMMMMMN     ",
          "                       ......$... ...... O..................,.....$MMMMMMMMMMMMN        ",
          "                       .....M.......... M M.. .............. 8  .OMMMMMMMMMMMN          ",
          "                        ..=7I,,.,,IMI...M.................. ..MMMMMMMMMMM               ",
          "                        ....DMMMMMMMMMMMMMMMO..............D...MMMMMMMMM                ",
          "                         .MMMMMMMMMMMMMMDDMM:,N..............DMMMMMMMMMMM               ",
          "                         NMMMMMNMM8 . .... ...,~............  MMMMMMMMM                 ",
          "                         MMMMM,:......::~..M8M8MM...............MMMMMM                  ",
          "                         MMMM ... . .........,MM..............MMMMMO$                   ",
          "                         MMMMM... =.=. .. . . MM ....... . ...MMMMMMM                   ",
          "                          NMMMMMMMMMM?  ..O.?NM7 ....... ......MMMMMM                   ",
          "                           NMMMMMMMMMMMMMMMMM........  $ . ...MMMNMMM                   ",
          "                            MMMMMMMMMMMMMMM.........,, ......MMMMMMMM                   ",
          "                             OMMMMMMMM8 , .. .. .,N.... ...:MMMMMMMMMMN                 ",
          "                              MMMMMMMM?N. ...~MD.:MNI8MMMMMMMMMMMMMMMMMN                ",
          "                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN              ",
          "                      NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN             ",
          "                     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN        ",
          "                  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM     ",
          "               MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM    ",
          "              NMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  ",
          "             MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM "]


def chucks_words_of_wisdom():
    print("Chuck here never quits\n")
    for chunk in chucky: print(chunk)
    print("Here is a flying phrase from Chuck to make you think twice next time:")
    cn = ChuckNorris()
    norris = cn.random()
    print(norris.joke)
