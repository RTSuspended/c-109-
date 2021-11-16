import pandas as pd
import statistics
import csv
df=pd.read_csv("height-weight.csv")
heightlist=df["Height(Inches)"].tolist()
weightlist=df["Weight(Pounds)"].tolist()
hmean=statistics.mean(heightlist)
hmedian=statistics.median(heightlist)
hmode=statistics.mode(heightlist)
hstdv=statistics.stdev(heightlist)
print("mean,median,mode of height is{},{},{} and {}".format(hmean,hmedian,hmode,hstdv))
height_first_standard_deviation_start,height_first_standard_deviation_end=hmean-hstdv,hmean+hstdv
height_second_standard_deviation_start,height_second_standard_deviation_end=hmean-2*hstdv,hmean+2*hstdv
height_third_standard_deviation_start,height_third_standard_deviation_end=hmean-3*hstdv,hmean+3*hstdv

heightlistofdatawithinfirststdv=[result for result in heightlist if result>height_first_standard_deviation_start and result<height_first_standard_deviation_end]
heightlistofdatawithinsecondstdv=[result for result in heightlist if result>height_second_standard_deviation_start and result<height_second_standard_deviation_end]
heightlistofdatawithinthirdstdv=[result for result in heightlist if result>height_third_standard_deviation_start and result<height_third_standard_deviation_end]

print("{}% of data lies within first standard deviation range".format(len(heightlistofdatawithinfirststdv)*100/len(heightlist)))
print("{}% of data lies within second standard deviation range".format(len(heightlistofdatawithinsecondstdv)*100/len(heightlist)))
print("{}% of data lies within third standard deviation range".format(len(heightlistofdatawithinthirdstdv)*100/len(heightlist)))

wmean=statistics.mean(weightlist)
wmedian=statistics.median(weightlist)
wmode=statistics.mode(weightlist)
wstdv=statistics.stdev(weightlist)
print("mean,median,mode of height is{},{},{} and {}".format(wmean,wmedian,wmode,wstdv))
weight_first_standard_deviation_start,weight_first_standard_deviation_end=wmean-wstdv,wmean+wstdv
weight_second_standard_deviation_start,weight_second_standard_deviation_end=wmean-2*wstdv,wmean+2*wstdv
weight_third_standard_deviation_start,weight_third_standard_deviation_end=wmean-3*wstdv,wmean+3*wstdv

weightlistofdatawithinfirststdv=[result for result in weightlist if result>weight_first_standard_deviation_start and result<weight_first_standard_deviation_end]
weightlistofdatawithinsecondstdv=[result for result in weightlist if result>weight_second_standard_deviation_start and result<weight_second_standard_deviation_end]
weightlistofdatawithinthirdstdv=[result for result in weightlist if result>weight_third_standard_deviation_start and result<weight_third_standard_deviation_end]

print("{}% of data lies within first standard deviation range".format(len(weightlistofdatawithinfirststdv)*100/len(weightlist)))
print("{}% of data lies within second standard deviation range".format(len(weightlistofdatawithinsecondstdv)*100/len(weightlist)))
print("{}% of data lies within third standard deviation range".format(len(weightlistofdatawithinthirdstdv)*100/len(weightlist)))