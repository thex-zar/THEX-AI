[app]
title = THEX
package.name = thex
package.domain = com.thex.app
source.dir =.
version = 1.0

requirements = python3==3.11.6,kivy==2.3.0
p4a.branch = v2024.1.21
android.api = 33
android.minapi = 21
android.ndk = 27
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.build_tools_version = 33.0.2
android.minapi = 21
p4a.branch = master
android.accept_sdk_license_agreement = True
