from pygame import mixer
import PySimpleGUI as sg
import random
import sys


# Audio setup
mixer.init()
audio_files = {
    "Attempt Arrest": "audio_files\Attempt_Arrest.mp3",
    "Awaiting Input": "audio_files\Awaiting_Input.mp3",
    "Crime": "audio_files\Crime.mp3",
    "Door": "audio_files\Door.mp3",
    "Escape": "audio_files\Escape.mp3",
    "Floor": "audio_files\Floor.mp3",
    "Incorrect Location": "audio_files\Incorrect_Location.mp3",
    "No_Movement": "audio_files\\No_Movement.mp3",
    "Street": "audio_files\Street.mp3",
    "Subway": "audio_files\Subway.mp3",
    "Tip": "audio_files\Tip.mp3",
    "Tipline": "audio_files\Tipline.mp3",
    "Window": "audio_files\Window.mp3"
}


# Dictionary of thief names and wanted values
thief_list = {
    "Armand Slinger": 900,
    "Bunny & Clod": 1000,
    "Emil 'The Cat' Donovan": 800,
    "Felicia Field": 900,
    "Hans Offe": 900,
    "John Doe": 800,
    "Luke Warm": 1000,
    "Ruby Diamond": 800,
    "Saul Teen": 1000,
    "The Brain": 1000,
}


# Create a dictionary of valid moves
valid_moves_dict = {
    "0": {
        "General Location": "None",
        "Space Type": "None",
        "Valid Moves": ["None"],
    },"113": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["123","124","503"],
    },
    "117": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["126","127","128","507"],
    },
    "123": {
        "General Location": "Building 1",
        "Space Type": "Crime",
        "Valid Moves": ["113","124","132"],
    },
    "124": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["113","123","125"],
    },
    "125": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["124","126","136"],
    },
    "126": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["125","127","136","117"],
    },
    "127": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["117","126","128","136"],
    },
    "128": {
        "General Location": "Building 1",
        "Space Type": "Window",
        "Valid Moves": ["117","127","519","539"],
    },
    "131": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["132","142","630"],
    },
    "132": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["123","131","142"],
    },
    "136": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["125","126","127","146","147"],
    },
    "142": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["131","132","151","152","153"],
    },
    "144": {
        "General Location": "Building 1",
        "Space Type": "Crime",
        "Valid Moves": ["153","154"],
    },
    "146": {
        "General Location": "Building 1",
        "Space Type": "Crime",
        "Valid Moves": ["136","147","157"],
    },
    "147": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["146","148","157","136"],
    },
    "148": {
        "General Location": "Building 1",
        "Space Type": "Window",
        "Valid Moves": ["147","157","539","559"],
    },
    "151": {
        "General Location": "Building 1",
        "Space Type": "Window",
        "Valid Moves": ["142","152","162","650"],
    },
    "152": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["142","151","153","162"],
    },
    "153": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["142","144","152","154","162","164"],
    },
    "154": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["144","153","164","165"],
    },
    "157": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["146","147","148","166","167","168"],
    },
    "162": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["151","152","153","171","172","173"],
    },
    "164": {
        "General Location": "Building 1",
        "Space Type": "Crime",
        "Valid Moves": ["154","165","173","153"],
    },
    "165": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["154","164","166","176"],
    },
    "166": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["157","165","167","176"],
    },
    "167": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["157","166","168","176"],
    },
    "168": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["157","167","559","579"],
    },
    "171": {
        "General Location": "Building 1",
        "Space Type": "Window",
        "Valid Moves": ["162","172","182","670"],
    },
    "172": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["162","171","173","182"],
    },
    "173": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["162","164","172","182"],
    },
    "176": {
        "General Location": "Building 1",
        "Space Type": "Floor",
        "Valid Moves": ["165","166","167","185"],
    },
    "182": {
        "General Location": "Building 1",
        "Space Type": "Door",
        "Valid Moves": ["171","172","173","591","593"],
    },
    "185": {
        "General Location": "Building 1",
        "Space Type": "Window",
        "Valid Moves": ["176","595"],
    },
    "214": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["223","225","703","705"],
    },
    "217": {
        "General Location": "Building 2",
        "Space Type": "Window",
        "Valid Moves": ["226","227","228","707"],
    },
    "223": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["214","233"],
    },
    "225": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["214","226","235"],
    },
    "226": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["217","225","227","235","237"],
    },
    "227": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["217","226","228","237"],
    },
    "228": {
        "General Location": "Building 2",
        "Space Type": "Window",
        "Valid Moves": ["217","227","237","619","639"],
    },
    "231": {
        "General Location": "Building 2",
        "Space Type": "Window",
        "Valid Moves": ["242","630"],
    },
    "233": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["223","242"],
    },
    "235": {
        "General Location": "Building 2",
        "Space Type": "Window",
        "Valid Moves": ["225","226","245"],
    },
    "237": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["226","227","228","247"],
    },
    "242": {
        "General Location": "Building 2",
        "Space Type": "Crime",
        "Valid Moves": ["231","233","251","252"],
    },
    "245": {
        "General Location": "Building 2",
        "Space Type": "Crime",
        "Valid Moves": ["235","255"],
    },
    "247": {
        "General Location": "Building 2",
        "Space Type": "Crime",
        "Valid Moves": ["237","257"],
    },
    "251": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["242","252","650"],
    },
    "252": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["242","251","263"],
    },
    "255": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["245","265"],
    },
    "257": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["247","267","268"],
    },
    "263": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["252","272","273","274"],
    },
    "265": {
        "General Location": "Building 2",
        "Space Type": "Crime",
        "Valid Moves": ["255","274","275","276"],
    },
    "267": {
        "General Location": "Building 2",
        "Space Type": "Crime",
        "Valid Moves": ["257","268","276"],
    },
    "268": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["257","267","659","679"],
    },
    "271": {
        "General Location": "Building 2",
        "Space Type": "Window",
        "Valid Moves": ["272","282","670"],
    },
    "272": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["263","271","273","282"],
    },
    "273": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["263","272","274","282","284"],
    },
    "274": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["263","265","273","275","284"],
    },
    "275": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["265","274","276","284","286"],
    },
    "276": {
        "General Location": "Building 2",
        "Space Type": "Floor",
        "Valid Moves": ["265","267","275","286"],
    },
    "282": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["271","272","273","691","693"],
    },
    "284": {
        "General Location": "Building 2",
        "Space Type": "Window",
        "Valid Moves": ["273","274","275","693","695"],
    },
    "286": {
        "General Location": "Building 2",
        "Space Type": "Door",
        "Valid Moves": ["275","276","695","697"],
    },
    "314": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["324","325","703","705"],
    },
    "317": {
        "General Location": "Building 3",
        "Space Type": "Window",
        "Valid Moves": ["326","327","328","707"],
    },
    "324": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["314","325","333"],
    },
    "325": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["314","324","326"],
    },
    "326": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["317","325","327","337"],
    },
    "327": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["317","326","328","337"],
    },
    "328": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["317","327","337","719","739"],
    },
    "331": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["332","342","830"],
    },
    "332": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["331","333","342"],
    },
    "333": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["324","332","342","344"],
    },
    "337": {
        "General Location": "Building 3",
        "Space Type": "Crime",
        "Valid Moves": ["326","327","328","347"],
    },
    "342": {
        "General Location": "Building 3",
        "Space Type": "Window",
        "Valid Moves": ["331","332","333","351","352"],
    },
    "344": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["333","345","354","355"],
    },
    "345": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["344","354","355"],
    },
    "347": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["337","357","358"],
    },
    "351": {
        "General Location": "Building 3",
        "Space Type": "Window",
        "Valid Moves": ["342","352","362","850"],
    },
    "352": {
        "General Location": "Building 3",
        "Space Type": "Crime",
        "Valid Moves": ["342","351","362"],
    },
    "354": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["344","345","355","365"],
    },
    "355": {
        "General Location": "Building 3",
        "Space Type": "Crime",
        "Valid Moves": ["344","345","354","365"],
    },
    "357": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["347","358","367"],
    },
    "358": {
        "General Location": "Building 3",
        "Space Type": "Window",
        "Valid Moves": ["347","357","367","759"],
    },
    "362": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["351","352","371","372","373"],
    },
    "365": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["354","355","374","375","376"],
    },
    "367": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["357","358","376"],
    },
    "371": {
        "General Location": "Building 3",
        "Space Type": "Window",
        "Valid Moves": ["362","372","870"],
    },
    "372": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["362","371","373"],
    },
    "373": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["362","372","374","384"],
    },
    "374": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["373","375","384"],
    },
    "375": {
        "General Location": "Building 3",
        "Space Type": "Floor",
        "Valid Moves": ["365","374","376","384","386"],
    },
    "376": {
        "General Location": "Building 3",
        "Space Type": "Crime",
        "Valid Moves": ["365","367","375","386"],
    },
    "384": {
        "General Location": "Building 3",
        "Space Type": "Window",
        "Valid Moves": ["373","374","375","793","795"],
    },
    "386": {
        "General Location": "Building 3",
        "Space Type": "Door",
        "Valid Moves": ["375","376","795","797"],
    },
    "413": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["423","424","503"],
    },
    "423": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["413","424","432"],
    },
    "424": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["413","423","425"],
    },
    "425": {
        "General Location": "Building 4",
        "Space Type": "Crime",
        "Valid Moves": ["424","426"],
    },
    "426": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["425","427","437"],
    },
    "427": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["426","428","437"],
    },
    "428": {
        "General Location": "Building 4",
        "Space Type": "Window",
        "Valid Moves": ["427","437","819","839"],
    },
    "432": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["423","441","442","443"],
    },
    "437": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["426","427","428","446","447","448"],
    },
    "441": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["432","442","452","830","850"],
    },
    "442": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["432","441","443","452"],
    },
    "443": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["432","442","444","452"],
    },
    "444": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["443","445"],
    },
    "445": {
        "General Location": "Building 4",
        "Space Type": "Crime",
        "Valid Moves": ["444","446","456"],
    },
    "446": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["437","445","447","456"],
    },
    "447": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["437","446","448","456"],
    },
    "448": {
        "General Location": "Building 4",
        "Space Type": "Window",
        "Valid Moves": ["437","447","839","859"],
    },
    "452": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["441","442","443","463"],
    },
    "456": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["445","446","447","465","466","467"],
    },
    "463": {
        "General Location": "Building 4",
        "Space Type": "Crime",
        "Valid Moves": ["452","464","472"],
    },
    "464": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["463","465"],
    },
    "465": {
        "General Location": "Building 4",
        "Space Type": "Crime",
        "Valid Moves": ["456","464","466"],
    },
    "466": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["456","465","467","477"],
    },
    "467": {
        "General Location": "Building 4",
        "Space Type": "Crime",
        "Valid Moves": ["456","466","468","477"],
    },
    "468": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["467","477","859","879"],
    },
    "471": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["472","482","870"],
    },
    "472": {
        "General Location": "Building 4",
        "Space Type": "Floor",
        "Valid Moves": ["463","471","482"],
    },
    "477": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["466","467","468","487"],
    },
    "482": {
        "General Location": "Building 4",
        "Space Type": "Window",
        "Valid Moves": ["472","891","893","471"],
    },
    "487": {
        "General Location": "Building 4",
        "Space Type": "Door",
        "Valid Moves": ["477","897"],
    },
    "500": {
        "General Location": "Street 5",
        "Space Type": "Subway",
        "Valid Moves": ["501","599","610","699","701","799","810","899"],
    },
    "501": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["500","503"],
    },
    "503": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["113","413","501","505"],
    },
    "505": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["503","507"],
    },
    "507": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["117","505","509"],
    },
    "509": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["507","519","819"],
    },
    "519": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["128","509","539"],
    },
    "539": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["128","148","519","559"],
    },
    "559": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["148","168","539","579"],
    },
    "579": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["168","559","599"],
    },
    "591": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["182","593","690"],
    },
    "593": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["182","591","595"],
    },
    "595": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["185","593","597"],
    },
    "597": {
        "General Location": "Street 5",
        "Space Type": "Street",
        "Valid Moves": ["595","599"],
    },
    "599": {
        "General Location": "Street 5",
        "Space Type": "Subway",
        "Valid Moves": ["500","579","597","699","799","899"],
    },
    "610": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["500","630"],
    },
    "619": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["228","639","709"],
    },
    "630": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["131","231","610","650"],
    },
    "639": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["228","619","659"],
    },
    "650": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["151","251","630","670"],
    },
    "659": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["268","639","679"],
    },
    "670": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["171","271","650","690"],
    },
    "679": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["268","659","699"],
    },
    "690": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["591","670","691"],
    },
    "691": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["282","690","693"],
    },
    "693": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["282","284","691","695"],
    },
    "695": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["284","286","693","697"],
    },
    "697": {
        "General Location": "Street 6",
        "Space Type": "Street",
        "Valid Moves": ["286","695","699"],
    },
    "699": {
        "General Location": "Street 6",
        "Space Type": "Subway",
        "Valid Moves": ["500","599","679","697","799","899"],
    },
    "701": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["500","703"],
    },
    "703": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["214","314","701","705"],
    },
    "705": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["214","314","703","707"],
    },
    "707": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["217","317","705","709"],
    },
    "709": {
        "General Location": "Street 7",
        "Space Type": "Crime",
        "Valid Moves": ["619","707","719"],
    },
    "719": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["328","709","739"],
    },
    "739": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["328","719","759"],
    },
    "759": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["358","739","779"],
    },
    "779": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["759","799"],
    },
    "791": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["793","890"],
    },
    "793": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["384","791","795"],
    },
    "795": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["384","386","793","797"],
    },
    "797": {
        "General Location": "Street 7",
        "Space Type": "Street",
        "Valid Moves": ["386","795","799"],
    },
    "799": {
        "General Location": "Street 7",
        "Space Type": "Subway",
        "Valid Moves": ["500","599","699","779","797","899"],
    },
    "810": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["500","830"],
    },
    "819": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["428","509","839"],
    },
    "830": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["331","441","810","850"],
    },
    "839": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["428","448","819","859"],
    },
    "850": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["351","441","830","870"],
    },
    "859": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["448","468","839","879"],
    },
    "870": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["371","471","850","890"],
    },
    "879": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["468","859","899"],
    },
    "890": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["791","870","891"],
    },
    "891": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["482","890","893"],
    },
    "893": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["482","891","895"],
    },
    "895": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["893","897"],
    },
    "897": {
        "General Location": "Street 8",
        "Space Type": "Street",
        "Valid Moves": ["487","895","899"],
    },
    "899": {
        "General Location": "Street 8",
        "Space Type": "Subway",
        "Valid Moves": ["500","599","699","799","879","897"],
    },
}

# List of all Subway spaces (where Thief can 'teleport' around board)
subway_spaces = ["500", "599", "699", "799", "899"]

# List of all starting crime spaces (where a thief can begin)
thief_starting_crime_spaces = ["123", "144", "146", "164", "242", "245", "247", "265", "267", "337", "352", "355", "376", "425", "445", "467", "463"]


# Thief class - name, wanted value, captured status, additional crimes, current location
class Thief:
    # Initialize thief class
    def __init__(self):
        self._move_dictionary = valid_moves_dict.copy()
        self._name = random.choice(list(thief_list.keys()))
        self._starting_reward = thief_list.get(self._name)
        self._additional_crimes = 0
        self._succesful_escapes = 0
        self._starting_space = random.choice(list(thief_starting_crime_spaces))
        # self._starting_space = "123" # !!! ONLY during testing, remove and use the random function just above for live
        self._move_history = [self._starting_space]
        self._current_general_location = self._move_dictionary[self._move_history[-1]]["General Location"]
        self._current_space = self._starting_space
    # Return the thief name
    def __str__(self):
        return self._name
    # Return original wanted amount
    def get_starting_reward(self):
        return self._starting_reward
    # Return the total reward amount
    def get_total_reward(self):
        return self._starting_reward + (self._additional_crimes * 100) + (self._succesful_escapes * 100)
    # Return additional crime count
    def get_additional_crime_count(self):
        return self._additional_crimes
    # Increase escape count
    def increase_escape_count(self):
        self._succesful_escapes += 1
    # Return escape count
    def get_escape_count(self):
        return self._succesful_escapes
    # Return general starting location (Building Number)
    def get_general_starting_location(self):
        starting_building = self._move_dictionary[self._move_history[0]]["General Location"]
        return starting_building
    # Add new thief move to history
    def add_move_to_list(self, space_number):
        self._move_history.append(space_number)
        # Convert committed crime spaces to floor spaces
        if self._move_dictionary[space_number]['Space Type'] == 'Crime':
            self._move_dictionary[space_number]['Space Type'] = 'Crime_Committed'
            self._additional_crimes += 1
        # Check if thief changed 'general' location
        if self._current_general_location != self._move_dictionary[self._move_history[-1]]["General Location"]:
            # reset any previously committed crime spaces if true
            for space_number in self._move_history:
                if self._move_dictionary[space_number]['Space Type'] == 'Crime_Committed':
                    self._move_dictionary[space_number]['Space Type'] = 'Crime'
            self._current_general_location = self._move_dictionary[self._move_history[-1]]["General Location"]
    # Return general location (Building/Street Number)
    def get_general_location(self):
        return self._current_general_location
    # Return thief current space type
    def get_space_type(self):
        if self._move_dictionary[self._move_history[-1]]['Space Type'] == 'Crime_Committed':
            return 'Floor'
        else:
            return self._move_dictionary[self._move_history[-1]]['Space Type']
    # Return thief exact location
    def get_exact_location(self):
        return self._move_history[-1]
    # Return thief previous space
    def get_previous_location(self):
        if len(self._move_history) == 1:
            return self._move_history
        else:
            return self._move_history[-2]
    # Return thief move history
    def get_move_history(self):
        move_history_types_raw = []
        for space_number in self._move_history:
            space_type = self._move_dictionary[space_number]["Space Type"]
            move_history_types_raw.append(space_type)
            move_history_types_edited = ' -> '.join(move_history_types_raw)
            move_history_types_combined = self.get_general_starting_location() + " " + move_history_types_edited
        return move_history_types_combined
    # Return valid thief moves
    def get_valid_moves(self):
        return self._move_dictionary[self._move_history[-1]]['Valid Moves']
    # Return thief debug move history
    def get_debug_move_history(self):
        return self._move_history


def main():
    # Main game menu PySimpleGUI themes and window layout
    sg.theme('Black')
    game_menu_layout = [
        [sg.Text("Welcome to the game!")],
        [sg.Text("How many human players?")],
        [sg.Radio("2", "num_players", key='2'), sg.Radio("3", "num_players", key='3'), sg.Radio("4", "num_players", key='4')],
        [sg.Button('Play Game'), sg.Button('Quit Game')]
    ]
    game_menu_window = sg.Window("Game Menu", game_menu_layout, enable_close_attempted_event=True).finalize()
    while True:
        gui_event, gui_values = game_menu_window.read()
        if gui_event == 'Play Game' and not (gui_values['2'] or gui_values['3'] or gui_values['4']):
            continue
        if (gui_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or gui_event == 'Exit') and sg.popup_yes_no('Do you really want to exit the game?') == 'Yes':
            sys.exit()
        if gui_event == "Quit Game":
            sys.exit()
        if gui_event == 'Play Game':
            if gui_values['2']:
                number_players = 2
            elif gui_values['3']:
                number_players = 3
            elif gui_values['4']:
                number_players = 4
            game_menu_window.close()
            winner, thief = play_game(number_players)
            print("Congratulations to Player " + str(winner) + " on catching " + str(thief) + " with an original reward of $" + str(thief.get_starting_reward()) + ".")
            print("They committed " + str(thief.get_additional_crime_count() + 1) + " total crimes and escaped arrest " + str(thief.get_escape_count()) + " total times.")
            print("Their final arrest reward is $" + str(thief.get_total_reward()))
            print()


def play_game(number_players):
    # Create a new thief from the wanted list and set the starting crime space
    new_thief = Thief()
    # Announce the general starting location for the thief and starting reward
    audio_file = mixer.Sound(audio_files["Crime"])
    audio_file.play()
    line1 = ("A new thief named " + str(new_thief) + " has been detected committing a crime somehwere in " + new_thief.get_general_starting_location() + ".")
    line2 = ("Their current arrest reward is: $" + str(new_thief.get_starting_reward()))
    message = line1 + "" + "\n" + line2
    sg.popup(message, title="New Thief Detected", button_color="white on blue", font=("Helvetica", 12), keep_on_top=True)
    # Set the current player number to start with player 1
    player_number = 1
    # Players take turns until the thief is arrested
    while True:
        # player turn
        winner = player_turn(new_thief, player_number)
        if winner == True:
            return player_number, new_thief
        # next player
        player_number += 1
        # Reset to player 1 after last player turn
        if player_number > number_players:
            player_number = 1
    return


def player_turn(new_thief, player_number):
    sg.theme('Dark')
    player_turn_layout = [
        [sg.Text("Current thief move history : ", key='thief history')],
        [sg.Text("Debug history : ", key='debug history')],
        [sg.Text("Player ???, it is your turn. What would you like to do?", key='player number')],
        [sg.Text("You used your free clue this turn, only select 'Clue' if you are allowed another clue on your same turn.", visible=False, key='clue used')],
        [sg.Radio("Clue", "choice", key='Clue', default=True), sg.Radio("Tip", "choice", key='Tip'), sg.Radio("Attempt Arrest", "choice", key='Attempt Arrest'), sg.Radio("End Turn", "choice", key='End Turn', disabled=True)],
        [sg.Text("You must at least receive a clue or attempt an arrest before ending your turn.", key='end_turn_disabled')],
        [sg.Button('Submit')]
    ]
    player_turn_window = sg.Window("Player Turn", player_turn_layout, enable_close_attempted_event=True).finalize()
    while True:
        thief_move_history = "Thief move history: " + str(new_thief.get_move_history())
        player_turn_number = "Player " + str(player_number) + ", it is your turn. What would you like to do?"
        debug_turn_history = new_thief.get_debug_move_history()
        player_turn_window['thief history'].update(thief_move_history)
        player_turn_window['player number'].update(player_turn_number)
        player_turn_window['debug history'].update(debug_turn_history)
        player_turn_window.refresh()
        gui_event, gui_values = player_turn_window.read()
        if (gui_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or gui_event == 'Exit') and sg.popup_yes_no('Do you really want to exit the game?') == 'Yes':
            sys.exit()
        if gui_event == 'Submit' and not (gui_values['Clue'] or gui_values['Tip'] or gui_values['Attempt Arrest']or gui_values['End Turn']):
            continue
        # Player chooses to get a clue
        if gui_event == 'Submit' and gui_values['Clue'] and not player_turn_window['clue used'].visible:
            thief_move(new_thief)
            # Update clue note to be visible, only get 1 'free' clue each turn per player
            player_turn_window['clue used'].update(visible=True)
            player_turn_window['End Turn'].update(disabled=False)
            player_turn_window['end_turn_disabled'].update(visible=False)
            # player_turn_window['Clue'].update(False)
            player_turn_window['End Turn'].update(True)
        elif gui_event == 'Submit' and gui_values['Clue'] and player_turn_window['clue used'].visible:
            thief_move(new_thief)
            # player_turn_window['Clue'].update(False)
            player_turn_window['End Turn'].update(True)
        # Player chooses to get a tip
        if gui_event == 'Submit' and gui_values['Tip']:
            player_turn_window.hide()
            get_tip(new_thief, player_number)
            player_turn_window.un_hide()
            # player_turn_window['Tip'].update(False)
            player_turn_window['End Turn'].update(True)
        # Player chooses to attempt an arrest
        if gui_event == 'Submit' and gui_values['Attempt Arrest']:
            player_turn_window.hide()
            arrest_result = attempt_arrest(new_thief)
            player_turn_window.un_hide()
            if arrest_result == True:
                return True
            else:
                player_turn_window['Attempt Arrest'].update(False)
                return
        # Player chooses to end their turn
        if gui_event == 'Submit' and gui_values['End Turn']:
            player_turn_window.close()
            return
    player_turn_window.close()
    return


def thief_move(new_thief):
    # Check if thief last turn ended on Subway space to trigger special move rule
    if new_thief.get_space_type() == 'Subway':
        new_location = random.choice(subway_spaces)
    # Random chance thief does not move
    if random.randint(1, 100) < 5: # !!! need to figure out a good %
        sg.popup("The Thief remains at their current location this turn", title="Did not move", button_color="white on blue", font=("Helvetica", 12), keep_on_top=True)
        audio_file = mixer.Sound(audio_files["No_Movement"])
        audio_file.play()
        return
    # Get the thieves current space valid moves list so we can temporarily modify it if needed
    valid_moves_list = new_thief.get_valid_moves()
    # Remove previous location if its in the valid moves list because the 'thief does not backtrack'
    if new_thief.get_previous_location() in valid_moves_list:
        valid_moves_list.remove(new_thief.get_previous_location())
    # If there is an available nearby crime space to move to, that must be the choice
    for space_number in valid_moves_list:
        if new_thief.get_space_type() == 'Crime':
            new_location = space_number
    # Randomly pick a new space to move to and move
        else:
            new_location = random.choice(valid_moves_list)
    new_thief.add_move_to_list(new_location)
    # Get space type and play appropiate sound effect
    if new_thief.get_space_type() == "Crime":
        audio_file = mixer.Sound(audio_files["Crime"])
    elif new_thief.get_space_type() == "Floor":
        audio_file = mixer.Sound(audio_files["Floor"])
    elif new_thief.get_space_type() == "Door":
        audio_file = mixer.Sound(audio_files["Door"])
    elif new_thief.get_space_type() == "Window":
        audio_file = mixer.Sound(audio_files["Window"])
    elif new_thief.get_space_type() == "Street":
        audio_file = mixer.Sound(audio_files["Street"])
    elif new_thief.get_space_type() == "Subway":
        audio_file = mixer.Sound(audio_files["Subway"])
    audio_file.play()
    message = "The Thief has moved to a " + new_thief.get_space_type() + ' space.'
    sg.popup(message, title="Did not move", button_color="white on blue", font=("Helvetica", 12), keep_on_top=True)
    return


def get_tip(new_thief, player_number):
    sg.theme('Dark')
    get_tip_layout = [
        [sg.Text("Warning, the TIP you are about to receive is for player " + str(player_number) + "'s eyes ONLY!")],
        [sg.Text("Press 'OK' to receive the TIP or press 'CANCEL' to return to the previous screen")],
        [sg.Button('OK'), sg.Button('CANCEL')]
    ]
    get_tip_window = sg.Window("Tipster Hotline", get_tip_layout, enable_close_attempted_event=True).finalize()
    audio_file = mixer.Sound(audio_files["Tipline"])
    audio_file.play()
    while True:
        gui_event, gui_values = get_tip_window.read()
        if (gui_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or gui_event == 'Exit') and sg.popup_yes_no('Do you really want to exit the game?') == 'Yes':
            sys.exit()
        if gui_event == 'CANCEL':
           get_tip_window.close()
           break
        if gui_event == 'OK':
            audio_file = mixer.Sound(audio_files["Tip"])
            audio_file.play()
            message = "TIP RECEIVED! Thief exact location is: " + str(new_thief.get_exact_location())
            sg.popup(message, title="TIP", button_color="white on blue", font=("Helvetica", 12), keep_on_top=True)
            break
    get_tip_window.close()
    return


def attempt_arrest(new_thief):
    sg.theme('Dark')
    attempt_arrest_layout = [
        [sg.Text("Indicate where you would like to attempt to make an arrest...")],
        [sg.Text("Example 1: For Building 1 Space 23 you would enter: 123")],
        [sg.Text("Example 2: For Street 6-70 you would enter: 670")],
        [sg.Input(key="arrest_space")],
        [sg.Text("Press 'Submit' to attempt the arrest or press 'Cancel' to return to the previous screen")],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]
    attempt_arrest_window = sg.Window("Attempt Arrest", attempt_arrest_layout, enable_close_attempted_event=True).finalize()
    audio_file = mixer.Sound(audio_files["Awaiting Input"])
    audio_file.play()
    while True:
        gui_event, gui_values = attempt_arrest_window.read()
        if (gui_event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or gui_event == 'Exit') and sg.popup_yes_no('Do you really want to exit the game?') == 'Yes':
            sys.exit()
        if gui_event == 'Cancel':
           attempt_arrest_window.close()
           break
        if gui_event == 'Submit':
            audio_file = mixer.Sound(audio_files["Attempt Arrest"])
            audio_file.play()
            arrest_space = int(gui_values['arrest_space'])
            if int(new_thief.get_exact_location()) == int(arrest_space):
                if random.randint(1, 100) < 95: # !!! need to figure out a good %
                    audio_file = mixer.Sound(audio_files["Incorrect Location"])
                    audio_file.play()
                    sg.popup("The Thief escaped your arrest attempt! They're getting away...", title="Escape Arrest", button_color="white on blue", font=("Helvetica", 12), keep_on_top=True)
                    extra_moves = random.randint(5, 6)
                    for i in range(extra_moves):
                        thief_move(new_thief)
                    attempt_arrest_window.close()
                    return False
                else:
                    attempt_arrest_window.close()
                    return True
            else:
                audio_file = mixer.Sound(audio_files["Incorrect Location"])
                audio_file.play()
                sg.popup("Wrong location, False Arrest, lose a turn", title="False Arrest", button_color="white on blue", font=("Helvetica", 12), keep_on_top=True)
                attempt_arrest_window.close()
                return False


if __name__ == "__main__":
    main()