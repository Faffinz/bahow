#!/bin/env python
#
#	stack overflow 10059594
#
import pandas as pd 
import pprint 
#
#		cookbook chapter 6
#
import csv
from collections import namedtuple
#
#
#

class Classifier():
    data = None
    class_attr = None
    priori = {}
    cp = {}
    hypothesis = None


    def __init__(self,filename=None, class_attr=None ):
        self.data = pd.read_csv(filename, sep=',', header =(0))
        self.class_attr = class_attr

    '''
        probability(class) =    How many  times it appears in cloumn
                             __________________________________________
                                  count of all class attribute
    '''
    def calculate_priori(self):
        class_values = list(set(self.data[self.class_attr]))
#        print "clasat", self.class_attr, ' :listDAT: ', set(self.data[self.class_attr])
#        exit()
        class_data =  list(self.data[self.class_attr])
        for i in class_values:
            self.priori[i]  = class_data.count(i)/float(len(class_data))
        #print "Priori Values: ", self.priori

    '''
        Here we calculate the individual probabilites 
        P(outcome|evidence) =   P(Likelihood of Evidence) x Prior prob of outcome
                               ___________________________________________
                                                    P(Evidence)
    '''
    def get_cp(self, attr, attr_type, class_value):
        data_attr = list(self.data[attr])
        class_data = list(self.data[self.class_attr])
        total = 1
        for i in range(0, len(data_attr)):
            if class_data[i] == class_value and data_attr[i] == attr_type:
                total += 1
        return total/float(class_data.count(class_value))

    '''
        Here we calculate Likelihood of Evidence and multiple all individual probabilities with priori
        (Outcome|Multiple Evidence) = P(Evidence1|Outcome) x P(Evidence2|outcome) x ... x P(EvidenceN|outcome) x P(Outcome)
        scaled by P(Multiple Evidence)
    '''
    def calculate_conditional_probabilities(self, hypothesis):
        for i in self.priori:
            self.cp[i] = {}
            for j in hypothesis:
                self.cp[i].update({ hypothesis[j]: self.get_cp(j, hypothesis[j], i)})
        #print "\nCalculated Conditional Probabilities: \n"
        #pprint.pprint(self.cp)

    def classify(self):
        resultd = { '1f':0.0, '2f':0.0, '3f':0.0, '4f':0.0, '0f':0.0 }
        #print "Result: "
        for i in self.cp:
        #    print i, " ==> ", reduce(lambda x, y: x * y, self.cp[i].values()) * self.priori[i] * 100000000.0
            resultd[i]  = reduce(lambda x, y: x * y, self.cp[i].values()) * self.priori[i]
# * 100000000000.0
        #for x in ( '1f', '2f', '3f', '4f', '0f', ):
        #    print x, resultd[x]
        return resultd
'''

#class csv_read(file)
#        with open(filename) as fin:
#            fin_csv = csv.reader(fin)
#            headers = next(fin_csv)
'''
class Mystifier():
    data = None
    class_attr = None
    priori = {}
    cp = {}
    hypothesis = None


    def __init__(self,filename=None ):
        self.data = pd.read_csv(filename, sep = ',', header = (0), usecols = [ 'HORSEN', 'TRAINER', 'JOCKY', 'VABM', 'PXR', 'PVF', 'PVAB', 'PQRA', 'PTIP', 'PAF', 'DTB', 'LS1' ] )
#        self.data = pd.read_csv(filename, sep = ',', header = (0), usecols = [ 'TRAINER', 'JOCKY', 'VABM', 'PXR', 'PVF', 'PVAB', 'PQRA', 'PTIP', 'PFPO', 'PAF', 'TBAR', 'DTB' ] )
        
#        self.class_attr = class_attr



if __name__ == "__main__":
    #c = Classifier(filename="new_dataset.csv", class_attr="Buys_Computer" )
    #c = Classifier(filename="data.csv", class_attr="Buys_Computer" )
    #c = Classifier(filename = "ca.csv", class_attr = "PAF" )
    c = Classifier(filename = "train.csv", class_attr = "PAF" )
    #c = Classifier(filename = "/tmp/xh.csv", class_attr = "PAF" )
    c.calculate_priori()
#    exit()

'''
    #c.hypothesis = {"Age":'<=30', "Income":"medium", "Student":'yes' , "Creadit_Rating":'fair'}
    c.hypothesis = { "JOCKY":'J LLOYD', "JORA":'j', "VABM":'b', "PXR":1, "PVF":1, "PVAB":8, "PQRA":'4q', "PTIP":'4t', "PFPO":'2s' }
###"Age":'<=30', "Income":"medium", "Student":'yes' , "Creadit_Rating":'fair'}

    c.calculate_conditional_probabilities(c.hypothesis)
    ltd = c.classify()
    
    for x in ( '1f', '2f', '3f', '4f', '0f', ):
        print x, ltd[x]
    
    print "\n++++++++++++ comes third +++++++++++++++=\n"
    

    c.hypothesis = { "JOCKY":'L CASSIDY', "JORA":'j', "VABM":'b', "PXR":5, "PVF":2, "PVAB":10, "PQRA":'3q', "PTIP":'0t', "PFPO":'4s'  }
    c.calculate_conditional_probabilities(c.hypothesis)
    ltd = c.classify()
#
#		this is prints results like i need
#
    for x in ( '1f', '2f', '3f', '4f', '0f', ):
        print "%s %6.3f" %(x, ltd[x])
    print '\n==================================================================\n'
    m = Mystifier(filename="ta.csv" )
#
#		this is NOT what i need
#
#    print "%s" %( m.data.to_string(index = False))
#/////////////    print "YYYYYYYYYYYYYYYYYYYYYYYYaaaaaaaaaaaaaa",m.data.columns, "\n????????gives column names???????\n"
#
#	this gives data like i need
#
#    for yuc in  m.data.values:		#itertuples():
#        print "\n!!!!!!!!!\n%s" %(yuc)

#[ 'PAF','PQRA','PXR','PVF','PVAB','PTIP'                                     ]]                                                    #(m.data["PAF"] == '1f' ) ]
#m.data.to_string(index = False)
#    print "YYYYYYYuuuuuuuuuCCCCCCCCC", yuc
    opstr = "%s"
    for valu in m.data.values:
        print valu[0:],"valu 0",valu[0:1],valu[1:2],valu[2:3].tostring()
        opstr = "'%s':'%s'" %("JOCKY",valu[0:1],"VABM",valu[1:2],"PXR",valu[2:3],"PVF",valu[3:4],"PVAB",valu[4:5],"PQRA",valu[6:7],"PTIP",valu[7:8])
        print opstr, "OPSTR"
'''
#
#
###m = Mystifier(filename="ta.csv" )
###W = m.data.to_dict()
###print W
###exit()
#
#
'''

this part gets the picture.

#fin_thing = {}
with open("ta.csv" )as fin:
        fin_csv = csv.reader(fin)
        fin_header = next(fin_csv)
        #print "FIN_HEADER", fin_header
        fin_thing = { 'JOCKY':'','VABM':'','PXR':'','PVF':'','PQRA':'','PTIP':'' }
        FINro = namedtuple("Row", fin_header, rename = True)
        for ro_ro in fin_csv:
            fin_ro = FINro( *ro_ro)
            #print fin_ro
            fin_thing['JOCKY'] = fin_ro.JOCKY
            fin_thing['VABM'] = fin_ro.VABM
            fin_thing['PXR'] = fin_ro.PXR
            fin_thing['PVF'] = fin_ro.PVF
            fin_thing['PQRA'] = fin_ro.PQRA
            fin_thing['PTIP'] = fin_ro.PTIP
            #fin_thing['JOCKY'] = fin_ro.JOCKY
            #print "???????", fin_thing
            actual_fin = fin_ro.PAF
            c.hype = fin_thing
            c.calculate_conditional_probabilities(c.hype)
            ltd = c.classify()
            stot = 0.0
#            strt = 0.0
#            strt = reduce((lambda a , b: a + b), ltd[ '0f','1f','2f','3f','4f', ] ) #for x in ( '1f', '2f', '3f', '4f', '0f', ):
            for x in ( '1f', '2f', '3f', '4f', '0f', ):
                stot += ltd[x]
            for x in ( '1f', '2f', '3f', '4f', '0f', ):
                ltd[x] = stot / ltd[x]
#            print '                   Actual result:', actual_fin, '\n'
            for x in ( '1f', '2f', '3f', '4f', '0f', ):
                if x == actual_fin:
                    print "%s %5.2f %s %s %s %s %s" %(x, ltd[x], fin_thing, "Qw:",fin_ro.QWIN, "Fw:",fin_ro.FWIN)
                else:
                    print "%s %5.2f" %(x, ltd[x])
#            print '                   Actual result:', actual_fin, '\n'
#            print "STOT",stot, "STRT",strt
            #
            #
            #exit()
            #
            #
#
'''
testfile = 'ta.csv'
testfile = '/tmp/test.csv'
with open( testfile )as fin:
        #print "%17s%7s %8s %8s %8s %8s %12s %10s %3s %3s %3s %3s" %( ' ', '1f', '2f', '3f', '4f', '0f', 'JOCKY', 'VF', 'VAB', 'QRA', 'XR', 'TIP' )
        print "      R#:h# %16s%8s %8s %12s %13s %3s %3s %3s %3s %s %s" %( ' ', '1f', '0f', 'JOCKY', 'VF', 'VAB', 'QRA', 'XR', 'TIP', ' ', 'TRAINER' )
        fin_thing = { 'JOCKY':'','VABM':'','PXR':'','PVF':'','PVAB':'','PQRA':'','PTIP':'', 'TRAINER':'', 'DTB':'', 'LS1':'' }
        fin_csv = csv.reader(fin)
        fin_header = next(fin_csv)
        #print "FIN_HEADER", fin_header
        FINro = namedtuple( "Row", fin_header )
        #print FINro._fields
        for ro_ro in fin_csv:
            fin_ro = FINro( *ro_ro )
            #print fin_ro
            if fin_ro.JOCKY.lower() == "scratched":
                ltd['0f'] = 0.01
                ltd['1f'] = 0.01
                continue
            fin_thing['JOCKY'] = fin_ro.JOCKY
            fin_thing['VABM'] = fin_ro.VABM
            fin_thing['PXR'] = fin_ro.PXR
            fin_thing['PVF'] = fin_ro.PVF
            fin_thing['PVAB'] = fin_ro.PVAB
            fin_thing['PQRA'] = fin_ro.PQRA
            fin_thing['PTIP'] = fin_ro.PTIP
            fin_thing['TRAINER'] = fin_ro.TRAINER
            fin_thing['DTB'] = fin_ro.DTB
            fin_thing['LS1'] = fin_ro.LS1
            #print "???????", fin_thing
            #actual_fin = fin_ro.PAF
            c.hype = fin_thing
            c.calculate_conditional_probabilities(c.hype)
            ltd = c.classify()
            stot = 0.0
            for x in ( '1f', '2f', '3f', '4f', '0f', ):
                stot += ltd[x]
#            for x in ( '1f', '2f', '3f', '4f', '0f', ):
#            ltd['1f'] = stot / ltd['1f']
#            ltd['0f'] = stot / (ltd['2f']+ltd['3f']+ltd['4f']+ltd['0f'])
            for x in ( '1f', '2f', '3f', '4f', '0f', ):
                ltd[x] = stot / ltd[x]
            if ltd['0f'] >  99999.0:
                ltd['0f'] = 99999.0
            if fin_ro.JOCKY.lower() == "scratched":
                ltd['0f'] = 0.01
                ltd['1f'] = 0.01
                #ltd['2f'] = 0.0
                #ltd['3f'] = 0.0
                #ltd['4f'] = 0.0
            #print " %17s %6.2f %8.2f %8.2f %8.2f %8.2f %2s %-15s %3s %3s %3s %3s %3s %s" %( fin_ro.HORSENAM, ltd['1f'], ltd['2f'], ltd['3f'], ltd['4f'], ltd['0f'], \
			#' ', fin_ro.JOCKY, fin_ro.PVF, fin_ro.PVAB, fin_ro.PQRA, fin_ro.PXR, fin_ro.PTIP, fin_ro.TRAINER )
            print "%5s%2s:%2s: %18s %6.2f %8.2f %2s %-18s %3s %3s %3s %3s %3s %s" %(fin_ro.VEN,fin_ro.TRN,fin_ro.HORSEN, fin_ro.HORSENAM, ltd['1f'], ltd['0f'], \
			' ', fin_ro.JOCKY, fin_ro.PVF, fin_ro.PVAB, fin_ro.PQRA, fin_ro.PXR, fin_ro.PTIP, fin_ro.TRAINER )
#            print '                   Actual result:', actual_fin, '\n'
            #print len(  )

            #for x in ( '1f', '2f', '3f', '4f', '0f', ):
            #    else:
            #        print "%s %5.2f" %(x, ltd[x])
            #
            #
            #exit()
            #
            #
#
        #
# train on 			ca.csv
# tst on         ta.csv
exit()
    
    
    
    
    
    
    
    
  
    
    
#    
    
    
    
    
    
    
    
    
    
'''    
    exit()
    exit()
    exit()
    exit()
    exit()
    exit()
    exit()
    exit()
'''
#    for ta in list(m.data['JOCKY'], m.data['VABM'], m.data['PXR'], m.data['PVF'], m.data['PVAB'], m.data['PQRA'], m.data['PTIP'], m.data['PFPO']):
#    for ta in m.data['JOCKY'], m.data['VABM'], m.data['PXR'], m.data['PVF'], m.data['PVAB'], m.data['PQRA'], m.data['PTIP'], m.data['PFPO']:
#    for ta in m.data.to_string():
#['JOCKY'], m.data['VABM'], m.data['PXR'], m.data['PVF'], m.data['PVAB'], m.data['PQRA'], m.data['PTIP'], m.data['PFPO']:
#        print "%s" %(ta)
#, m.data['VABM'], m.data['PXR'], m.data['PVF'], m.data['PVAB'], m.data['PQRA'], m.data['PTIP'], m.data['PFPO']:)
#        pass
#        pass
#        pass
#        pass
#        pass        class_values = list(set(self.data[self.class_attr]))
#                    class_data =  list(self.data[self.class_attr])

#        pass
#        pass
#    m = Mystifier(filename="td.csv", class_attr="PAF" )




'''
ert Heathcote,L CASSIDY,j,50.1,b,5,2,10,13.0,14.6,3.2,WTC ,2f,3q,0t,4s,4u
by Edmonds,J LLOYD,j,27.7,b,10,1,6,9.00,7.3,2.7, ,1f,2q,0t,5s,5u


    c.hypothesis = { 
"JORA":
'j', 
"VABM":
'b', 
"PXR":
1, 
"PVF":
1, 
"PVAB":
8, 
"PQRA":
'4q', 
"PTIP":
'4t', 
"PFPO":
'2s', 
"PTABO":
'2u'
 }


3,SCST,20161130,BR,Sunshine Coast,10,HANDICAP,1600,20000,Raining,Good,04,8,10,54.5,11,x83,X,8,3,SPIRIT MINDED,(Eagle Farm),Robert Heathcote,N DAY,j,48.5,a,6,4,1,10.0,11.1,2.6,WT ,0f,2q,2t,3s,3u
3,SCST,20161130,BR,Sunshine Coast,10,HANDICAP,1600,20000,Raining,Good,04,9,12,54.0,04,x21,X,2,1,PRINCESS CHARM,(Eagle Farm),Tony Gollan,R FRADD,j,55.1,a,3,5,3,2.80,2.6,1.4, ,3f,1q,1t,1s,1u
3,SCST,20161130,BR,Sunshine Coast,10,HANDICAP,1600,20000,Raining,Good,04,10,21,54.0,08,232,2,3,2,WICKED TRILOGY,(Eagle Farm),Robert Heathcote,L CASSIDY,j,50.1,b,5,2,10,13.0,14.6,3.2,WTC ,2f,3q,0t,4s,4u
3,SCST,20161130,BR,Sunshine Coast,10,HANDICAP,1600,20000,Raining,Good,04,11,14,54.0,05,321,3,2,1,BIANTIC,(Gold Coast),Toby Edmonds,J LLOYD,j,61.0,b,1,1,8,3.60,3.5,1.9,TC ,1f,4q,4t,2s,2u
3,SCST,20161130,BR,Sunshine Coast,10,HANDICAP,1600,20000,Raining,Good,04,12,14,54.0,13,188,1,8,8,CALL ME RUSTY,(Sunshine Coast),Stewart Mackinnon,S LACY,a,51.4,b,4,8,12,101.,71.2,13.5,WTC ,0f,6q,0t,10s,13u
3,SCST,20161130,BR,Sunshine Coast,10,HANDICAP,1600,20000,Raining,Good,04,13,15,54.0,07,533,5,3,3,RUBY RAY,(Bundaberg),Mary Hassam,M HELLYER,j,61.0,a,1,3,5,151.,70.6,11.5,DW ,0f,9q,0t,11s,12u

3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,1,14,59.0,09,x13,X,1,3,INGEEGOODBE,(Eagle Farm),Robert Heathcote,L CASSIDY,j,55.0,a,5,2,3,5.00,5.1,1.4,W ,0f,1q,3t,3s,4u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,2,14,59.0,07,234,2,3,4,LIGHTNING BELL,(Eagle Farm),Kelso Wood,B PENGELLY,j,60.2,a,2,4,1,5.50,4.8,1.7, ,0f,5q,0t,4s,3u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,3,10,58.5,05,332,3,3,2,TONY BALONEY,(Toowoomba),Tony Sears,MICHAEL CAHILL,j,58.9,a,3,3,5,3.40,4.1,1.6,W ,3f,3q,1t,1s,2u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,4,11,58.0,10,272,2,7,2,EMPRESS ZHAO (NZ),(Sunshine Coast),Kevin Sempf,S LACY,a,51.6,a,8,5,2,18.0,21.8,5.1, ,0f,6q,4t,6s,7u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,5,18,58.0,08,321,3,2,1,SWEET SHAMROCK (NZ),(Gold Coast),Toby Edmonds,J LLOYD,j,27.7,b,10,1,6,9.00,7.3,2.7, ,1f,2q,0t,5s,5u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,6,18,56.0,02,833,8,3,3,LA LA ROCK,(Toowoomba),Phyllis Kalinowski,S BOGENHUBER,j,53.0,b,7,6,8,67.0,45.0,10.8,W ,0f,6q,0t,8s,8u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,7,14,56.0,06,422,4,2,2,ROSADOR,(Toowoomba),John Dann,J ORMAN,j,61.3,a,1,3,4,4.20,3.9,1.5,WC ,2f,4q,2t,2s,1u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,8,10,55.5,03,423,4,2,3,LATE PAYMENT,(Deagon),Pat Duff,JASON TAYLOR,j,57.8,b,4,4,7,26.0,20.1,4.6, ,4f,4q,0t,7s,6u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,9,11,55.0,01,964,9,6,4,REGAL LAD,(Beaudesert),Laurie Richardson,B AINSWORTH,a,19.6,b,11,7,9,81.0,74.8,16.0,W ,0f,7q,0t,9s,9u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,10,10,54.0,04,0x8,0,X,8,COLD AS ICE,(Wondai),Peter Blackwell,R PAYNE,a,36.7,b,9,9,10,251.,184.2,37.8, ,0f,9q,0t,10s,11u
3,SCST,20161130,BR,Sunshine Coast,11,CLASS 1 HANDICAP,1600,20000,Raining,Good,04,11,14,54.0,11,788,7,8,8,STAINER (NZ),(Sunshine Coast),Trevor Miller,N THOMAS,j,53.2,b,6,8,11,251.,127.2,29.5,WC ,0f,8q,0t,10s,10u

3,SCST,20161130,BR,Sunshine Coast,12,F&M CLASS 1 HANDICAP,1200,20000,Raining,Good,04,1,14,60.0,03,x32,X,3,2,SHEEZALADY,(Eagle Farm),Robert Heathcote,T BROOKER,a,54.1,b,4,7,6,5.00,4.2,1.4,D ,4f,2q,4t,2s,3u
3,SCST,20161130,BR,Sunshine Coast,12,F&M CLASS 1 HANDICAP,1200,20000,Raining,Good,04,2,21,58.0,06,3x1,3,X,1,WINDY SANDS (NZ),(Eagle Farm),Barry Baldwin,C SCHMIDT,a,46.8,b,10,3,7,7.50,7.8,1.6,D ,3f,3q,0t,3s,4u
3,SCST,20161130,BR,Sunshine Coast,12,F&M CLASS 1 HANDICAP,1200,20000,Raining,Good,04,8,31,55.5,02,1 ,1, , ,FOX FORCE FIVE,(Eagle Farm),Liam Birchley,J ORMAN,j,51.1,a,8,1,2,3.00,3.9,1.5,C ,2f,4q,2t,1s,2u
3,SCST,20161130,BR,Sunshine Coast,12,F&M CLASS 1 HANDICAP,1200,20000,Raining,Good,04,9,29,55.0,05,12 ,1,2, ,PLUCKY GIRL,(Gold Coast),Toby Edmonds,J LLOYD,j,39.6,a,14,2,5,3.00,2.2,1.2, ,1f,1q,3t,1s,1u
3,SCST,20161130,BR,Sunshine Coast,12,F&M CLASS 1 HANDICAP,1200,20000,Raining,Good,04,10,25,54.5,04,x56,X,5,6,MARGO MAREE,(Deagon),Julie Green,M HELLYER,j,51.4,b,6,10,11,19.0,18.8,3.5,D ,0f,5q,0t,4s,5u
3,SCST,20161130,BR,Sunshine Coast,12,F&M CLASS 1 HANDICAP,1200,20000,Raining,Good,04,11,17,54.5,07,9x5,9,X,5,TRAMPERS,(Sunshine Coast),Andrew Williamson,MICHAEL CAHILL,j,52.1,b,5,7,10,81.0,71.0,10.9,D ,0f,6q,0t,6s,7u
3,SCST,20161130,BR,Sunshine Coast,12,F&M CLASS 1 HANDICAP,1200,20000,Raining,Good,04,12,12,54.0,01,x64,X,6,4,ARNHEM BEAUTY,(Doomben),Sherrie Lawlor,JASON TAYLOR,j,57.8,b,3,9,14,51.0,24.6,2.8,T ,0f,5q,0t,5s,6u
'''
