$app = "DeviceID"
$output = "builds/$app/apk"
$project = $app
$description = "Test for DeviceID"
$product = "DeviceID"
$company = "BytesRaw"
$copyright = "Copyright © 2024 BytesRaw"
$splashColor = "#1B575F"
$buildVersion = "1.0.{build}"

flet build apk $app --output $output --project $project --description $description --product $product --company $company --copyright $copyright --splash-color $splashColor --build-version $buildVersion