import requests
from bs4 import BeautifulSoup

'''
ds=input("Enter district:")
ps=input("Enter police station:")
y=input("Enter year:")
f_no=input("Enter FIR no.:")
'''
headers={'Content-Type':'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Host':'59.180.234.21:85'}
url = "http://59.180.234.21:85/index.aspx"

#payload="__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJMTQ2MDgwNjA1DxYCHgtUZW1wU3RhdGlvbgUHMDgxNjIwMRYCAgMPZBYCAgUPZBYEAgEPZBYIZg9kFgQCAQ9kFgICAQ8QZGQWAWZkAgMPZBYCAgEPEGRkFgBkAgEPZBYEAgEPZBYCAgEPEA8WBh4NRGF0YVRleHRGaWVsZAUIQ2l0eU5hbWUeDkRhdGFWYWx1ZUZpZWxkBQhDaXR5Q29kZR4LXyFEYXRhQm91bmRnZBAVEQwtLS1TRUxFQ1QtLS0NQ0VOVFJBTCBESVNUVBJDUklNRSBBTkQgUkFJTFdBWVMQRUFTVCBERUxISSBESVNUVAlJR0kgRElTVFQPTkVXIERFTEhJIERJU1RUC05PUlRIIERJU1RUEE5PUlRIIEVBU1QgRElTVFQQTk9SVEggV0VTVCBESVNUVAtPVVRFUiBESVNUVAtTT1VUSCBESVNUVBBTT1VUSCBFQVNUIERJU1RUEFNPVVRIIFdFU1QgRElTVFQSU1BFQ0lBTCBDRUxMIERJU1RUDlNQVVcgJiBDIERJU1RUCVZJR0lMQU5DRQpXRVNUIERJU1RUFREMLS0tU0VMRUNULS0tAzE2MgMxNjQDMTY4AzE2OQMxNjUDMTY2AzE3MwMxNzIDMTc0AzE2NwM5NTUDMTcxAzk1NAM5NTMDMTYxAzE3MBQrAxFnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgMPZBYCAgEPEA8WBh8BBQdQU19OYW1lHwIFB1BTX0NvZGUfA2dkEBUQDC0tLVNFTEVDVC0tLQxBTkFORCBQQVJCQVQOQ0hBTkRBTkkgTUFIQUwLRC5CLkcuIFJPQUQKREFSWUEgR0FOSglIQVVaIFFBWkkLSS5QLiBFU1RBVEULSkFNQSBNQVNKSUQKS0FNTEEgTUtULgpLQVJPTCBCQUdICk5BQkkgS0FSSU0KUEFIQVIgR0FOSgxQQVJTQUQgTkFHQVILUEFURUwgTkFHQVIOUkFKSU5ERVIgTkFHQVIMUkFOSklUIE5BR0FSFRAMLS0tU0VMRUNULS0tAjAxAjA4AjM4AjEwAjE1AjE2AjE5AjIzAjI2AjMwAjQxAjQwAjQyAjQ1AjU2FCsDEGdnZ2dnZ2dnZ2dnZ2dnZ2cWAQIBZAICD2QWBAIBD2QWAgIBDw8WAh4JTWF4TGVuZ3RoAgRkZAIDD2QWAgIBDxBkDxYIAgECAgIDAgQCBQIGAgcCCBYIEAUEMjAxOAUEMjAxOGcQBQQyMDE3BQQyMDE3ZxAFBDIwMTYFBDIwMTZnEAUEMjAxNQUEMjAxNWcQBQQyMDE0BQQyMDE0ZxAFBDIwMTMFBDIwMTNnEAUEMjAxMgUEMjAxMmcQBQQyMDExBQQyMDExZ2RkAgMPZBYEZg9kFgICAQ8QZGQWAQIDZAICD2QWAgIBDw8WAh4HRW5hYmxlZGhkZAIDD2QWBGYPZBYCZg9kFgICAw8PFgIeBFRleHQFDjFSZWNvcmRzIEZvdW5kZGQCAQ9kFgJmD2QWAgIBD2QWBAIBDzwrAAsBAA8WCB4IRGF0YUtleXMWAB4LXyFJdGVtQ291bnQCAR4VXyFEYXRhU291cmNlSXRlbUNvdW50AgEeCVBhZ2VDb3VudAIBZBYCZg9kFgYCAQ9kFgICCg8PFgIeB1Zpc2libGVoZGQCAg9kFhYCAQ8PFgIfBgUFMTc2NzhkZAICDw8WAh8GBQExZGQCAw8PFgIfBgUIMjAxMzAwMTJkZAIEDw8WAh8GBQQwMDEyZGQCBQ8PFgIfBgUEMjAxM2RkAgYPDxYCHwYFCjI2LTAxLTIwMTNkZAIHDw8WAh8GBQkwODE2MjAxICBkZAIIDw8WAh8GBQFBZGQCCQ8PFgIfBgUBTmRkAgoPDxYEHwYFA0FWQx8LaGRkAgwPZBYCAgEPDxYCHg9Db21tYW5kQXJndW1lbnQFCDIwMTMwMDEyZGQCAw9kFgICCg8PFgIfC2hkZAIDDzwrABEDAA8WBB8DZx8IZmQBEBYAFgAWAAwUKwAAZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUVRGdSZWdpc3QkY3RsMDIkQ2hrQWxsBRhEZ1JlZ2lzdCRjdGwwMyRDaGtTZWxlY3QFFkRnUmVnaXN0JGN0bDAzJGltZ3ZpZXcFGERnUmVnaXN0JGN0bDAzJGltZ0RlbGV0ZQUKZ3JkbXZ0aGVmdA88KwAMAQhmZOxGPTAfw24I2sQl2zU1m3zc49Q8oUJCzQ%2BR2WKROgru&__VIEWSTATEGENERATOR=90059987&__EVENTVALIDATION=%2FwEdADpV8MXKHKUwYoEqwZnu%2FxRvCsHRaAEHIr772zKgggdQ%2B5cM7ByNsRG4qWi12q7B1tveFDGmjlPiBn9IJO8m9jt8W1Wcqc3FqlgV9EENz1OdJenvj2TG96ujSrFeprbtr3RTWKEdLSZa5NFLztoz81urAMmLvBzV7Qyb4qeGafdxuGr4cVZnct4CZh3KKsvt%2BxdAs0fg094ls2%2BuRMaFDPjjvXQmtkg7agsuhug%2BxMVSXXqKkbM01pitokD3Lzhr%2F%2BZrc1JkJBoj%2BhAGr8ppVSNG4Yj6XkYB%2BZGeix5%2Budiv9J9IjbG0sujSnR9YEqeLFuIKGVNDezkrxdfUawGK33AxvjAuIFmExdxunofmSVMj2KhPcg%2F6G9KkHuC16bwbWAqSNP2Vcw4%2F0wky0Un3Ssd3cGZtjtv%2B8Amihean2n5uODEqvswSsIcl9%2BU0P3atZA9wwmGVjpLXO8otgZA9TTIB8lu5pTVNdmV8rh4nC22F1IV%2FFmxbqGixxW3jyfJHzf5JmvAxQ0TNsG%2FQBENv4FMPADgLnY9pn1HgIJ6W1oaeYdDWZw8Vw9V%2BwK94zhvV5AsFA%2BTourZKJXliwDtZTQ9ekaMKA7haZworGZv1GNL6jfGIOD9Z9b3s17WeWa7BrI8c9M3Y1nIZLhOjU%2F1XzSzL%2FxemvL%2BXvQqPhNDs1Wq9qbSJ3Q64XnqHJCqtILHuKInbZGapuyydv%2BNM8HQGHAYApdUpYoFh67eHvqG%2FzUcsUIah5HCoMOU8WaXO%2FxiJ%2BaHDwhBrj5fOr2ADFZqqi%2FZV6FwxLXIvJnnZxRCkEGL2vlv%2BEHwdfIYs6w%2BKmqOZx1qofpZfGzwk98LkdE4BMRqfb0u%2FQkGuYIFlLayujxQuRoo7FuDy7NXB14avq%2Fb2v7d2hTpZ2fAU%2FQNc8vV2rGQYBxmjLK%2FGwK%2B7fSfOvqbtXyWAlJYGhvsObwaNWBbmv0nimdfQ%2F7Zstm8F84f%2B3h9YyZaJR3dWRA9wpH6l11O4G2kmTb3SRnjBDgl28IWxIp0Fo2LO8gfTE%2FS%2Feu4xuwy3GO%2FLdWJ7sP3k941Xz%2BFQ%2B3gP4ao%2Bw4fjgSjZP4t9CTHAFY294D7izdoUMmVuRfNQ82teXMMssBplUFrOIVLaxLe7kUrdgDeNLJdISgOVUS%2BO1N1XNFmfsMXJasjxX85jwtRNxjBCVpIdQ3Jr3y1gfKY2XtUBVhps4vnAdjOpxanxSdZGygoJk116PGjZPJTmXL5g2ZXmPYUzhaqav9a4mAKiS8O7cr6eR16K79f6De8%3D&ddlDistrict=162&ddlPS=01&txtRegNo=12&ddlYear=2013&txRegFromDt=&txRegToDt=&rbtnListAVC=0&btnSearch=Search"
payload1 = [
    ("_EVENTTARGET", ""),
    ("_EVENTARGUMENT",""),
    ("_LASTFOCUS",""),
    ("_VIEWSTATE","/wEPDwUJMTQ2MDgwNjA1DxYCHgtUZW1wU3RhdGlvbgUHMDgxNjIwMRYCAgMPZBYCAgUPZBYEAgEPZBYIZg9kFgQCAQ9kFgICAQ8QZGQWAWZkAgMPZBYCAgEPEGRkFgBkAgEPZBYEAgEPZBYCAgEPEA8WBh4NRGF0YVRleHRGaWVsZAUIQ2l0eU5hbWUeDkRhdGFWYWx1ZUZpZWxkBQhDaXR5Q29kZR4LXyFEYXRhQm91bmRnZBAVEQwtLS1TRUxFQ1QtLS0NQ0VOVFJBTCBESVNUVBJDUklNRSBBTkQgUkFJTFdBWVMQRUFTVCBERUxISSBESVNUVAlJR0kgRElTVFQPTkVXIERFTEhJIERJU1RUC05PUlRIIERJU1RUEE5PUlRIIEVBU1QgRElTVFQQTk9SVEggV0VTVCBESVNUVAtPVVRFUiBESVNUVAtTT1VUSCBESVNUVBBTT1VUSCBFQVNUIERJU1RUEFNPVVRIIFdFU1QgRElTVFQSU1BFQ0lBTCBDRUxMIERJU1RUDlNQVVcgJiBDIERJU1RUCVZJR0lMQU5DRQpXRVNUIERJU1RUFREMLS0tU0VMRUNULS0tAzE2MgMxNjQDMTY4AzE2OQMxNjUDMTY2AzE3MwMxNzIDMTc0AzE2NwM5NTUDMTcxAzk1NAM5NTMDMTYxAzE3MBQrAxFnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgMPZBYCAgEPEA8WBh8BBQdQU19OYW1lHwIFB1BTX0NvZGUfA2dkEBUQDC0tLVNFTEVDVC0tLQxBTkFORCBQQVJCQVQOQ0hBTkRBTkkgTUFIQUwLRC5CLkcuIFJPQUQKREFSWUEgR0FOSglIQVVaIFFBWkkLSS5QLiBFU1RBVEULSkFNQSBNQVNKSUQKS0FNTEEgTUtULgpLQVJPTCBCQUdICk5BQkkgS0FSSU0KUEFIQVIgR0FOSgxQQVJTQUQgTkFHQVILUEFURUwgTkFHQVIOUkFKSU5ERVIgTkFHQVIMUkFOSklUIE5BR0FSFRAMLS0tU0VMRUNULS0tAjAxAjA4AjM4AjEwAjE1AjE2AjE5AjIzAjI2AjMwAjQxAjQwAjQyAjQ1AjU2FCsDEGdnZ2dnZ2dnZ2dnZ2dnZ2cWAQIBZAICD2QWBAIBD2QWAgIBDw8WAh4JTWF4TGVuZ3RoAgRkZAIDD2QWAgIBDxBkDxYIAgECAgIDAgQCBQIGAgcCCBYIEAUEMjAxOAUEMjAxOGcQBQQyMDE3BQQyMDE3ZxAFBDIwMTYFBDIwMTZnEAUEMjAxNQUEMjAxNWcQBQQyMDE0BQQyMDE0ZxAFBDIwMTMFBDIwMTNnEAUEMjAxMgUEMjAxMmcQBQQyMDExBQQyMDExZ2RkAgMPZBYEZg9kFgICAQ8QZGQWAQIDZAICD2QWAgIBDw8WAh4HRW5hYmxlZGhkZAIDD2QWBGYPZBYCZg9kFgICAw8PFgIeBFRleHQFDjFSZWNvcmRzIEZvdW5kZGQCAQ9kFgJmD2QWAgIBD2QWBAIBDzwrAAsBAA8WCB4IRGF0YUtleXMWAB4LXyFJdGVtQ291bnQCAR4VXyFEYXRhU291cmNlSXRlbUNvdW50AgEeCVBhZ2VDb3VudAIBZBYCZg9kFgYCAQ9kFgICCg8PFgIeB1Zpc2libGVoZGQCAg9kFhYCAQ8PFgIfBgUFMTc2NzhkZAICDw8WAh8GBQExZGQCAw8PFgIfBgUIMjAxMzAwMTJkZAIEDw8WAh8GBQQwMDEyZGQCBQ8PFgIfBgUEMjAxM2RkAgYPDxYCHwYFCjI2LTAxLTIwMTNkZAIHDw8WAh8GBQkwODE2MjAxICBkZAIIDw8WAh8GBQFBZGQCCQ8PFgIfBgUBTmRkAgoPDxYEHwYFA0FWQx8LaGRkAgwPZBYCAgEPDxYCHg9Db21tYW5kQXJndW1lbnQFCDIwMTMwMDEyZGQCAw9kFgICCg8PFgIfC2hkZAIDDzwrABEDAA8WBB8DZx8IZmQBEBYAFgAWAAwUKwAAZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUVRGdSZWdpc3QkY3RsMDIkQ2hrQWxsBRhEZ1JlZ2lzdCRjdGwwMyRDaGtTZWxlY3QFFkRnUmVnaXN0JGN0bDAzJGltZ3ZpZXcFGERnUmVnaXN0JGN0bDAzJGltZ0RlbGV0ZQUKZ3JkbXZ0aGVmdA88KwAMAQhmZOxGPTAfw24I2sQl2zU1m3zc49Q8oUJCzQ+R2WKROgru"),
    ("_VIEWSTATEGENERATOR","90059987"),
    ("_EVENTVALIDATION","/wEdADpV8MXKHKUwYoEqwZnu/xRvCsHRaAEHIr772zKgggdQ+5cM7ByNsRG4qWi12q7B1tveFDGmjlPiBn9IJO8m9jt8W1Wcqc3FqlgV9EENz1OdJenvj2TG96ujSrFeprbtr3RTWKEdLSZa5NFLztoz81urAMmLvBzV7Qyb4qeGafdxuGr4cVZnct4CZh3KKsvt+xdAs0fg094ls2+uRMaFDPjjvXQmtkg7agsuhug+xMVSXXqKkbM01pitokD3Lzhr/+Zrc1JkJBoj+hAGr8ppVSNG4Yj6XkYB+ZGeix5+udiv9J9IjbG0sujSnR9YEqeLFuIKGVNDezkrxdfUawGK33AxvjAuIFmExdxunofmSVMj2KhPcg/6G9KkHuC16bwbWAqSNP2Vcw4/0wky0Un3Ssd3cGZtjtv+8Amihean2n5uODEqvswSsIcl9+U0P3atZA9wwmGVjpLXO8otgZA9TTIB8lu5pTVNdmV8rh4nC22F1IV/FmxbqGixxW3jyfJHzf5JmvAxQ0TNsG/QBENv4FMPADgLnY9pn1HgIJ6W1oaeYdDWZw8Vw9V+wK94zhvV5AsFA+TourZKJXliwDtZTQ9ekaMKA7haZworGZv1GNL6jfGIOD9Z9b3s17WeWa7BrI8c9M3Y1nIZLhOjU/1XzSzL/xemvL+XvQqPhNDs1Wq9qbSJ3Q64XnqHJCqtILHuKInbZGapuyydv+NM8HQGHAYApdUpYoFh67eHvqG/zUcsUIah5HCoMOU8WaXO/xiJ+aHDwhBrj5fOr2ADFZqqi/ZV6FwxLXIvJnnZxRCkEGL2vlv+EHwdfIYs6w+KmqOZx1qofpZfGzwk98LkdE4BMRqfb0u/QkGuYIFlLayujxQuRoo7FuDy7NXB14avq/b2v7d2hTpZ2fAU/QNc8vV2rGQYBxmjLK/GwK+7fSfOvqbtXyWAlJYGhvsObwaNWBbmv0nimdfQ/7Zstm8F84f+3h9YyZaJR3dWRA9wpH6l11O4G2kmTb3SRnjBDgl28IWxIp0Fo2LO8gfTE/S/eu4xuwy3GO/LdWJ7sP3k941Xz+FQ+3gP4ao+w4fjgSjZP4t9CTHAFY294D7izdoUMmVuRfNQ82teXMMssBplUFrOIVLaxLe7kUrdgDeNLJdISgOVUS+O1N1XNFmfsMXJasjxX85jwtRNxjBCVpIdQ3Jr3y1gfKY2XtUBVhps4vnAdjOpxanxSdZGygoJk116PGjZPJTmXL5g2ZXmPYUzhaqav9a4mAKiS8O7cr6eR16K79f6De8=\%3D"),
    ("ddlDistrict", "162"),
    ("ddlPS", "01"),
    ("txtRegNo", "12"),
    ("ddlYear", "2013"),
    ("txRegFromDt", ""),
    ("txRegToDt", ""),
    ("rbtnListAVC", "0"),
]
#payload="__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJMTQ2MDgwNjA1DxYCHgtUZW1wU3RhdGlvbgUHMDgxNjIwMRYCAgMPZBYCAgUPZBYEAgEPZBYIZg9kFgQCAQ9kFgICAQ8QZGQWAWZkAgMPZBYCAgEPEGRkFgBkAgEPZBYEAgEPZBYCAgEPEA8WBh4NRGF0YVRleHRGaWVsZAUIQ2l0eU5hbWUeDkRhdGFWYWx1ZUZpZWxkBQhDaXR5Q29kZR4LXyFEYXRhQm91bmRnZBAVEQwtLS1TRUxFQ1QtLS0NQ0VOVFJBTCBESVNUVBJDUklNRSBBTkQgUkFJTFdBWVMQRUFTVCBERUxISSBESVNUVAlJR0kgRElTVFQPTkVXIERFTEhJIERJU1RUC05PUlRIIERJU1RUEE5PUlRIIEVBU1QgRElTVFQQTk9SVEggV0VTVCBESVNUVAtPVVRFUiBESVNUVAtTT1VUSCBESVNUVBBTT1VUSCBFQVNUIERJU1RUEFNPVVRIIFdFU1QgRElTVFQSU1BFQ0lBTCBDRUxMIERJU1RUDlNQVVcgJiBDIERJU1RUCVZJR0lMQU5DRQpXRVNUIERJU1RUFREMLS0tU0VMRUNULS0tAzE2MgMxNjQDMTY4AzE2OQMxNjUDMTY2AzE3MwMxNzIDMTc0AzE2NwM5NTUDMTcxAzk1NAM5NTMDMTYxAzE3MBQrAxFnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgMPZBYCAgEPEA8WBh8BBQdQU19OYW1lHwIFB1BTX0NvZGUfA2dkEBUQDC0tLVNFTEVDVC0tLQxBTkFORCBQQVJCQVQOQ0hBTkRBTkkgTUFIQUwLRC5CLkcuIFJPQUQKREFSWUEgR0FOSglIQVVaIFFBWkkLSS5QLiBFU1RBVEULSkFNQSBNQVNKSUQKS0FNTEEgTUtULgpLQVJPTCBCQUdICk5BQkkgS0FSSU0KUEFIQVIgR0FOSgxQQVJTQUQgTkFHQVILUEFURUwgTkFHQVIOUkFKSU5ERVIgTkFHQVIMUkFOSklUIE5BR0FSFRAMLS0tU0VMRUNULS0tAjAxAjA4AjM4AjEwAjE1AjE2AjE5AjIzAjI2AjMwAjQxAjQwAjQyAjQ1AjU2FCsDEGdnZ2dnZ2dnZ2dnZ2dnZ2cWAQIBZAICD2QWBAIBD2QWAgIBDw8WAh4JTWF4TGVuZ3RoAgRkZAIDD2QWAgIBDxBkDxYIAgECAgIDAgQCBQIGAgcCCBYIEAUEMjAxOAUEMjAxOGcQBQQyMDE3BQQyMDE3ZxAFBDIwMTYFBDIwMTZnEAUEMjAxNQUEMjAxNWcQBQQyMDE0BQQyMDE0ZxAFBDIwMTMFBDIwMTNnEAUEMjAxMgUEMjAxMmcQBQQyMDExBQQyMDExZ2RkAgMPZBYEZg9kFgICAQ8QZGQWAQIDZAICD2QWAgIBDw8WAh4HRW5hYmxlZGhkZAIDD2QWBGYPZBYCZg9kFgICAw8PFgIeBFRleHQFDjFSZWNvcmRzIEZvdW5kZGQCAQ9kFgJmD2QWAgIBD2QWBAIBDzwrAAsBAA8WCB4IRGF0YUtleXMWAB4LXyFJdGVtQ291bnQCAR4VXyFEYXRhU291cmNlSXRlbUNvdW50AgEeCVBhZ2VDb3VudAIBZBYCZg9kFgYCAQ9kFgICCg8PFgIeB1Zpc2libGVoZGQCAg9kFhYCAQ8PFgIfBgUFMTc2NzhkZAICDw8WAh8GBQExZGQCAw8PFgIfBgUIMjAxMzAwMTJkZAIEDw8WAh8GBQQwMDEyZGQCBQ8PFgIfBgUEMjAxM2RkAgYPDxYCHwYFCjI2LTAxLTIwMTNkZAIHDw8WAh8GBQkwODE2MjAxICBkZAIIDw8WAh8GBQFBZGQCCQ8PFgIfBgUBTmRkAgoPDxYEHwYFA0FWQx8LaGRkAgwPZBYCAgEPDxYCHg9Db21tYW5kQXJndW1lbnQFCDIwMTMwMDEyZGQCAw9kFgICCg8PFgIfC2hkZAIDDzwrABEDAA8WBB8DZx8IZmQBEBYAFgAWAAwUKwAAZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUVRGdSZWdpc3QkY3RsMDIkQ2hrQWxsBRhEZ1JlZ2lzdCRjdGwwMyRDaGtTZWxlY3QFFkRnUmVnaXN0JGN0bDAzJGltZ3ZpZXcFGERnUmVnaXN0JGN0bDAzJGltZ0RlbGV0ZQUKZ3JkbXZ0aGVmdA88KwAMAQhmZOxGPTAfw24I2sQl2zU1m3zc49Q8oUJCzQ%2BR2WKROgru&__VIEWSTATEGENERATOR=90059987&__EVENTVALIDATION=%2FwEdADpV8MXKHKUwYoEqwZnu%2FxRvCsHRaAEHIr772zKgggdQ%2B5cM7ByNsRG4qWi12q7B1tveFDGmjlPiBn9IJO8m9jt8W1Wcqc3FqlgV9EENz1OdJenvj2TG96ujSrFeprbtr3RTWKEdLSZa5NFLztoz81urAMmLvBzV7Qyb4qeGafdxuGr4cVZnct4CZh3KKsvt%2BxdAs0fg094ls2%2BuRMaFDPjjvXQmtkg7agsuhug%2BxMVSXXqKkbM01pitokD3Lzhr%2F%2BZrc1JkJBoj%2BhAGr8ppVSNG4Yj6XkYB%2BZGeix5%2Budiv9J9IjbG0sujSnR9YEqeLFuIKGVNDezkrxdfUawGK33AxvjAuIFmExdxunofmSVMj2KhPcg%2F6G9KkHuC16bwbWAqSNP2Vcw4%2F0wky0Un3Ssd3cGZtjtv%2B8Amihean2n5uODEqvswSsIcl9%2BU0P3atZA9wwmGVjpLXO8otgZA9TTIB8lu5pTVNdmV8rh4nC22F1IV%2FFmxbqGixxW3jyfJHzf5JmvAxQ0TNsG%2FQBENv4FMPADgLnY9pn1HgIJ6W1oaeYdDWZw8Vw9V%2BwK94zhvV5AsFA%2BTourZKJXliwDtZTQ9ekaMKA7haZworGZv1GNL6jfGIOD9Z9b3s17WeWa7BrI8c9M3Y1nIZLhOjU%2F1XzSzL%2FxemvL%2BXvQqPhNDs1Wq9qbSJ3Q64XnqHJCqtILHuKInbZGapuyydv%2BNM8HQGHAYApdUpYoFh67eHvqG%2FzUcsUIah5HCoMOU8WaXO%2FxiJ%2BaHDwhBrj5fOr2ADFZqqi%2FZV6FwxLXIvJnnZxRCkEGL2vlv%2BEHwdfIYs6w%2BKmqOZx1qofpZfGzwk98LkdE4BMRqfb0u%2FQkGuYIFlLayujxQuRoo7FuDy7NXB14avq%2Fb2v7d2hTpZ2fAU%2FQNc8vV2rGQYBxmjLK%2FGwK%2B7fSfOvqbtXyWAlJYGhvsObwaNWBbmv0nimdfQ%2F7Zstm8F84f%2B3h9YyZaJR3dWRA9wpH6l11O4G2kmTb3SRnjBDgl28IWxIp0Fo2LO8gfTE%2FS%2Feu4xuwy3GO%2FLdWJ7sP3k941Xz%2BFQ%2B3gP4ao%2Bw4fjgSjZP4t9CTHAFY294D7izdoUMmVuRfNQ82teXMMssBplUFrOIVLaxLe7kUrdgDeNLJdISgOVUS%2BO1N1XNFmfsMXJasjxX85jwtRNxjBCVpIdQ3Jr3y1gfKY2XtUBVhps4vnAdjOpxanxSdZGygoJk116PGjZPJTmXL5g2ZXmPYUzhaqav9a4mAKiS8O7cr6eR16K79f6De8%3D&ddlDistrict=162&ddlPS=01&txtRegNo=12&ddlYear=2013&txRegFromDt=&txRegToDt=&rbtnListAVC=0&btnSearch=Search"
pam="__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJMTQ2MDgwNjA1DxYCHgtUZW1wU3RhdGlvbgUHMDgxNjIwMRYCAgMPZBYCAgUPZBYEAgEPZBYIZg9kFgQCAQ9kFgICAQ8QZGQWAWZkAgMPZBYCAgEPEGRkFgBkAgEPZBYEAgEPZBYCAgEPEA8WBh4NRGF0YVRleHRGaWVsZAUIQ2l0eU5hbWUeDkRhdGFWYWx1ZUZpZWxkBQhDaXR5Q29kZR4LXyFEYXRhQm91bmRnZBAVEQwtLS1TRUxFQ1QtLS0NQ0VOVFJBTCBESVNUVBJDUklNRSBBTkQgUkFJTFdBWVMQRUFTVCBERUxISSBESVNUVAlJR0kgRElTVFQPTkVXIERFTEhJIERJU1RUC05PUlRIIERJU1RUEE5PUlRIIEVBU1QgRElTVFQQTk9SVEggV0VTVCBESVNUVAtPVVRFUiBESVNUVAtTT1VUSCBESVNUVBBTT1VUSCBFQVNUIERJU1RUEFNPVVRIIFdFU1QgRElTVFQSU1BFQ0lBTCBDRUxMIERJU1RUDlNQVVcgJiBDIERJU1RUCVZJR0lMQU5DRQpXRVNUIERJU1RUFREMLS0tU0VMRUNULS0tAzE2MgMxNjQDMTY4AzE2OQMxNjUDMTY2AzE3MwMxNzIDMTc0AzE2NwM5NTUDMTcxAzk1NAM5NTMDMTYxAzE3MBQrAxFnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgMPZBYCAgEPEA8WBh8BBQdQU19OYW1lHwIFB1BTX0NvZGUfA2dkEBUQDC0tLVNFTEVDVC0tLQxBTkFORCBQQVJCQVQOQ0hBTkRBTkkgTUFIQUwLRC5CLkcuIFJPQUQKREFSWUEgR0FOSglIQVVaIFFBWkkLSS5QLiBFU1RBVEULSkFNQSBNQVNKSUQKS0FNTEEgTUtULgpLQVJPTCBCQUdICk5BQkkgS0FSSU0KUEFIQVIgR0FOSgxQQVJTQUQgTkFHQVILUEFURUwgTkFHQVIOUkFKSU5ERVIgTkFHQVIMUkFOSklUIE5BR0FSFRAMLS0tU0VMRUNULS0tAjAxAjA4AjM4AjEwAjE1AjE2AjE5AjIzAjI2AjMwAjQxAjQwAjQyAjQ1AjU2FCsDEGdnZ2dnZ2dnZ2dnZ2dnZ2cWAQIBZAICD2QWBAIBD2QWAgIBDw8WAh4JTWF4TGVuZ3RoAgRkZAIDD2QWAgIBDxBkDxYIAgECAgIDAgQCBQIGAgcCCBYIEAUEMjAxOAUEMjAxOGcQBQQyMDE3BQQyMDE3ZxAFBDIwMTYFBDIwMTZnEAUEMjAxNQUEMjAxNWcQBQQyMDE0BQQyMDE0ZxAFBDIwMTMFBDIwMTNnEAUEMjAxMgUEMjAxMmcQBQQyMDExBQQyMDExZ2RkAgMPZBYEZg9kFgICAQ8QZGQWAQIDZAICD2QWAgIBDw8WAh4HRW5hYmxlZGhkZAIDD2QWBGYPZBYCZg9kFgICAw8PFgIeBFRleHQFDjFSZWNvcmRzIEZvdW5kZGQCAQ9kFgJmD2QWAgIBD2QWBAIBDzwrAAsBAA8WCB4IRGF0YUtleXMWAB4LXyFJdGVtQ291bnQCAR4VXyFEYXRhU291cmNlSXRlbUNvdW50AgEeCVBhZ2VDb3VudAIBZBYCZg9kFgYCAQ9kFgICCg8PFgIeB1Zpc2libGVoZGQCAg9kFhYCAQ8PFgIfBgUFMTc2NzhkZAICDw8WAh8GBQExZGQCAw8PFgIfBgUIMjAxMzAwMTJkZAIEDw8WAh8GBQQwMDEyZGQCBQ8PFgIfBgUEMjAxM2RkAgYPDxYCHwYFCjI2LTAxLTIwMTNkZAIHDw8WAh8GBQkwODE2MjAxICBkZAIIDw8WAh8GBQFBZGQCCQ8PFgIfBgUBTmRkAgoPDxYEHwYFA0FWQx8LaGRkAgwPZBYCAgEPDxYCHg9Db21tYW5kQXJndW1lbnQFCDIwMTMwMDEyZGQCAw9kFgICCg8PFgIfC2hkZAIDDzwrABEDAA8WBB8DZx8IZmQBEBYAFgAWAAwUKwAAZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WBAUVRGdSZWdpc3QkY3RsMDIkQ2hrQWxsBRhEZ1JlZ2lzdCRjdGwwMyRDaGtTZWxlY3QFFkRnUmVnaXN0JGN0bDAzJGltZ3ZpZXcFGERnUmVnaXN0JGN0bDAzJGltZ0RlbGV0ZQUKZ3JkbXZ0aGVmdA88KwAMAQhmZOxGPTAfw24I2sQl2zU1m3zc49Q8oUJCzQ%2BR2WKROgru&__VIEWSTATEGENERATOR=90059987&__EVENTVALIDATION=%2FwEdADpV8MXKHKUwYoEqwZnu%2FxRvCsHRaAEHIr772zKgggdQ%2B5cM7ByNsRG4qWi12q7B1tveFDGmjlPiBn9IJO8m9jt8W1Wcqc3FqlgV9EENz1OdJenvj2TG96ujSrFeprbtr3RTWKEdLSZa5NFLztoz81urAMmLvBzV7Qyb4qeGafdxuGr4cVZnct4CZh3KKsvt%2BxdAs0fg094ls2%2BuRMaFDPjjvXQmtkg7agsuhug%2BxMVSXXqKkbM01pitokD3Lzhr%2F%2BZrc1JkJBoj%2BhAGr8ppVSNG4Yj6XkYB%2BZGeix5%2Budiv9J9IjbG0sujSnR9YEqeLFuIKGVNDezkrxdfUawGK33AxvjAuIFmExdxunofmSVMj2KhPcg%2F6G9KkHuC16bwbWAqSNP2Vcw4%2F0wky0Un3Ssd3cGZtjtv%2B8Amihean2n5uODEqvswSsIcl9%2BU0P3atZA9wwmGVjpLXO8otgZA9TTIB8lu5pTVNdmV8rh4nC22F1IV%2FFmxbqGixxW3jyfJHzf5JmvAxQ0TNsG%2FQBENv4FMPADgLnY9pn1HgIJ6W1oaeYdDWZw8Vw9V%2BwK94zhvV5AsFA%2BTourZKJXliwDtZTQ9ekaMKA7haZworGZv1GNL6jfGIOD9Z9b3s17WeWa7BrI8c9M3Y1nIZLhOjU%2F1XzSzL%2FxemvL%2BXvQqPhNDs1Wq9qbSJ3Q64XnqHJCqtILHuKInbZGapuyydv%2BNM8HQGHAYApdUpYoFh67eHvqG%2FzUcsUIah5HCoMOU8WaXO%2FxiJ%2BaHDwhBrj5fOr2ADFZqqi%2FZV6FwxLXIvJnnZxRCkEGL2vlv%2BEHwdfIYs6w%2BKmqOZx1qofpZfGzwk98LkdE4BMRqfb0u%2FQkGuYIFlLayujxQuRoo7FuDy7NXB14avq%2Fb2v7d2hTpZ2fAU%2FQNc8vV2rGQYBxmjLK%2FGwK%2B7fSfOvqbtXyWAlJYGhvsObwaNWBbmv0nimdfQ%2F7Zstm8F84f%2B3h9YyZaJR3dWRA9wpH6l11O4G2kmTb3SRnjBDgl28IWxIp0Fo2LO8gfTE%2FS%2Feu4xuwy3GO%2FLdWJ7sP3k941Xz%2BFQ%2B3gP4ao%2Bw4fjgSjZP4t9CTHAFY294D7izdoUMmVuRfNQ82teXMMssBplUFrOIVLaxLe7kUrdgDeNLJdISgOVUS%2BO1N1XNFmfsMXJasjxX85jwtRNxjBCVpIdQ3Jr3y1gfKY2XtUBVhps4vnAdjOpxanxSdZGygoJk116PGjZPJTmXL5g2ZXmPYUzhaqav9a4mAKiS8O7cr6eR16K79f6De8%3D&ddlDistrict=162&ddlPS=01&txtRegNo=12&ddlYear=2013&txRegFromDt=&txRegToDt=&rbtnListAVC=0&btnSearch=Search"
r = requests.post(url=url,headers=headers, params=pam)

soup = BeautifulSoup(r.content, "html.parser")
#soup = BeautifulSoup(r.text, "lxml").text
print(soup)
letters=soup.find_all("tr",attrs={'class': 'DataItemStyle'})
print(letters)
'''
payload2=[ ("ddlDistrict", "162"),
    ("ddlPS", "01"),
    ("txtRegNo", "12"),
    ("ddlYear", "2013"),
    ("txRegFromDt", ""),
    ("txRegToDt", ""),
    ("rbtnListAVC", "0")
           ]
headers2={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Host':'59.180.234.21:85',"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate",'Referer':'http://59.180.234.21:85/index.aspx',"Cookie":"ASP.NET_SessionId=frv4ogay0itxseqvzmnnbrbk","Connection":"keep-alive"}
r1=requests.get(url="http://59.180.234.21:85/ReportViewer.aspx",headers=headers2)
#a2=BeautifulSoup(r1.text,"lxml").text
print(r1.json())


url3="chrome-extension://gmpljdlgcdkljlppaekciacdmdlhfeon/data/user-preferences-default.json"
headers3={'Content-Type':'application/json',"ETag":"4X2Ih2IQ2fVRhBijHEBG5BhTjGk=","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
r3=requests.get(url=url3,headers=headers3)
a3=BeautifulSoup(r3.content,"html.parser")
print(a3.prettify())
'''