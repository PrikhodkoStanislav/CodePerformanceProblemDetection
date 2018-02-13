import os

featuresFileName = "features.tsv"
featuresPSIFileName = "featuresPSI.tsv"
featuresUnifiedFileName = "featuresUnified.tsv"

numberOfPSIFeatures = 12
NaNLine = ('\t' + "NaN") * numberOfPSIFeatures

def feature_merger():
    try:
        featuresUnifiedFile = open(featuresUnifiedFileName, 'w')
        with open(featuresFileName, 'r') as featuresFile:
            features = featuresFile.readlines()
            with open(featuresPSIFileName, 'r') as featuresPSIFile:
                featuresPSI = featuresPSIFile.readlines()
                itr = iter(featuresPSI)
                s = next(itr)
                arrPSI = s.split('\t')
                idPSI = int(arrPSI[0])
                for line in features:
                    line = line.replace('\t' + "NaN", '')
                    line = line.rstrip()
                    featuresUnifiedFile.write(line)
                    arr = line.split('\t')
                    id = int(arr[0])
                    if idPSI == id:
                        for part in arrPSI[1:]:
                            part = part.rstrip()
                            featuresUnifiedFile.write('\t' + part)

                        s = next(itr)
                        arrPSI = s.split('\t')
                        idPSI = int(arrPSI[0])
                    else:
                        featuresUnifiedFile.write(NaNLine)
                    featuresUnifiedFile.write('\n')

        featuresUnifiedFile.close()
        featuresPSIFile.close()
        featuresFile.close()
    except:
        pass

feature_merger()