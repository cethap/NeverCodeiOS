import json

def runCommand(command):
    import subprocess
    bashCommand = command
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
    return output

def runCommandJson(command):
    return json.loads(runCommand(command))

data = runCommandJson("/Users/greenhouse/bin/aws devicefarm create-upload --project-arn arn:aws:devicefarm:us-west-2:655603536603:project:fc6f6e31-7c1e-49dd-b212-03739b00dcb1 --name Univision_com.univision.android.apk --type ANDROID_APP")
arnApp = data["upload"]["arn"]
urlApp = data["upload"]["url"]
runCommand('curl -T Univision_com.univision.android.apk '+urlApp)
data = runCommandJson('/Users/greenhouse/bin/aws devicefarm create-upload --project-arn arn:aws:devicefarm:us-west-2:655603536603:project:fc6f6e31-7c1e-49dd-b212-03739b00dcb1 --name test.zip --type APPIUM_JAVA_TESTNG_TEST_PACKAGE')
arnAut = data["upload"]["arn"]
urlAut = data["upload"]["url"]
runCommand('curl -T test.zip '+urlAut)

# arnApp = "arn:aws:devicefarm:us-west-2:655603536603:upload:fc6f6e31-7c1e-49dd-b212-03739b00dcb1/58aecb16-6f67-4d85-b2f0-bbe5524ebc7b"
# arnAut = "arn:aws:devicefarm:us-west-2:655603536603:upload:fc6f6e31-7c1e-49dd-b212-03739b00dcb1/00a1c169-e877-4723-8837-d8148ffab619"

devicePool = "arn:aws:devicefarm:us-west-2:655603536603:devicepool:fc6f6e31-7c1e-49dd-b212-03739b00dcb1/e7f54231-110f-467e-8238-a93da29336e0"
testStructure = "type=APPIUM_JAVA_TESTNG,testPackageArn="+arnAut+",testSpecArn=arn:aws:devicefarm:us-west-2::upload:4f8bd338-7be5-11e8-adc0-fa7ae01bbebc"
executionConfiguration = "jobTimeoutMinutes=150,videoCapture=true,skipAppResign=false"
data = runCommandJson('/Users/greenhouse/bin/aws devicefarm schedule-run --project-arn arn:aws:devicefarm:us-west-2:655603536603:project:fc6f6e31-7c1e-49dd-b212-03739b00dcb1 --app-arn '+arnApp+' --device-pool-arn '+devicePool+' --execution-configuration '+executionConfiguration+' --test '+testStructure)
print(data)
