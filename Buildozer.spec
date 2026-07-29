[app]

title = Gold Miner
package.name = goldminer
package.domain = com.miner
version = 1.0.0

requirements = python3==3.10,pygame,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

orientation = portrait
fullscreen = 1

android.api = 30
android.ndk = 23b
android.sdk = 30
android.minapi = 21
android.archs = armeabi-v7a

android.permissions = INTERNET

source.dir = .
source.include_exts = py,png,jpg

log_level = 2