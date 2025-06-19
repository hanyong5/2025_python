
import requests
import json


cookies = {
    'PCID': '16247705314370002565497',
    'MARKETID': '16247705314370002565497',
    'x-coupang-accept-language': 'ko-KR',
    '_fbp': 'fb.1.1739079230308.913915237482103068',
    'gd1': 'Y',
    'srp_delivery_toggle': 'true',
    'delivery_toggle': 'false',
    'x-coupang-target-market': 'KR',
    'sid': '8d4ed3a2517f4473b8e97d53bc2f25284379b851',
    'searchKeyword': '%EC%95%84%EC%9D%B4%ED%8F%B0%2015|%EC%95%84%EC%9D%B4%ED%8F%B015',
    'searchKeywordType': '{%22%EC%95%84%EC%9D%B4%ED%8F%B0%2015%22:0}|{%22%EC%95%84%EC%9D%B4%ED%8F%B015%22:0}',
    'trac_src': '1042016',
    'trac_spec': '10304903',
    'trac_addtag': '900',
    'trac_ctag': 'HOME',
    'trac_lptag': '%EC%BF%A0%ED%8C%A1',
    'trac_itime': '20250610111420',
    'bm_mi': 'B656D513F9B392973C8C0115DB8F5571~YAAQB9ojF9Wb1EKXAQAA2xSeVxwGC+qiTmMDyaHWlMhf8sA77a+62ty/6Mg2CGatqDuGRAP4+Hx9EEeZS4Tx3ZSkK2EnPe8iVaoxjbIPa4CvmTsP5O4UqLZHEn/MjfNUkD7vXjl1NQN5ZuHw78qM4tVMKgaa+dk3bS3sNZYZWT0kfy8txCIdXMoct4BkBa+1/ia3WRNbKjmfTB18os3/V+o/rq7QAmNQ3OAlzaDgHAqjakGIPYXgNFK7eoVR68S3ZiTkPHXzISV5PxY6QkjKljEkeMMoDypMwrIahtbuKnr/PJIsxZEA5KZEr3XtSmyDNvB8vq6cCqUflNoTO6uZt2Uwyg==~1',
    '_abck': '59D6E61C9FC8339D97112BB1FC3EEAD5~0~YAAQB9ojF5ic1EKXAQAAzxWeVw4yS6HewzqGRRQLyrlu8rq87QzUDW3MJ3hGwqS2/rDSz4FbBGlY4NijNJgBXfIq2hkVol8qF04dRoLCicsDC5TwHp4lMCogSfnyvB1BArSxyQbwRh4roiCcxNQnFXKoVgY9ov3wk/9cW71x5o8hUxTlZXeOfZNUGSbD72v3NACJTpYqTw6SGC+HUUGuNa9Ph00L6ZmfY2CAWvscxSQcOxn8ej1dMeLB+fz0LCyp05cX3SAmvdbDj3hK2MjP3g/Vj1jOqNMAd5ZnsmX54zsb2P2G7ImLD9s3EayqkQXBT/5fLnovjj7nsFD0Dja5SbY8c/eMZoVpbR4kg5O5wGJTs7gpkrlMho+KEkW5FX8XVC14gnLYSkeq4Mgx2GEBxh6Hs0z3SZL95B+CDok/wsHLULtnfD+vliELkh4NXjVbFpAwh53mOaaFRsYuvujJ01yLxqmxwAkO3dyW8Deu/I+wm0tFGNH+M1aj5LkADzxj7KkzhYXYsBuTLVNh0DPmB8Uck22Y3xLvRRs2Bg9W68+8zKxTpiqp79czYtTw9L3jDWre2VHQ9hjB6DJsC3BJhysxfgDg2VUO7RH9rGk21hEQ4fzJJ3i3u8felG6WKO+F60rnnCfya0ThT9sB4ERuc+JYGz7utB8rK5BR++fvcM54znegWMGl6KnzflGE0zVE7J687iVWMyLO8tQBVFX1Kf6/mF7bSMZ8QfyY4y9wk0WfEgvRiDO0K5M4+EEguktZmRY=~-1~-1~1749024683',
    'cto_bundle': 'CFmrv19hdzlqRzJkdE5RN09uOW1Vb2wzRTMzbWNaMVNUQTZUdzQyamFkSCUyRjdzOUZqVlY4VWF3cllCamtQeVE0UWQ0JTJGb1VXV2dHQ1dMSjc5bHVSc3l2VnRPdzc1R00lMkIlMkZaaERYd3VzQ3NlVkNxUSUyRmtFMEd4R3VHRTlTdTdOTFVMWmpuOXZ4bWV6VzdQaUElMkYxTDNmQyUyRkNza2VqMkF6OHZWSEgwMjJUUzNuNVZiMGptdVpTNlZOT2JVMFZsdHpKQ25qdnF6U0pNMUMlMkJnU0ZCV3ZUdTRmYiUyQk93RVVBJTNEJTNE',
    'ak_bmsc': '1BE11C51B47202E229EDDFD36D15FF68~000000000000000000000000000000~YAAQB9ojF9qr1EKXAQAANCmeVxwiL3oqcDIWTP8n2fSJjaBa/6/bDU+Mp8eVbwipnCXCOtLanVAlAog958fFn/lNm2P+wRMOSo5uUHo/ZlJBQy2a7aQjFQAk+0FuR0ntyKyr3BisBPyTAE83L3zZSFp/MvMW24WHROQAoiosIGbTvFJTsYnLrQoWmny4JkkxD4dLcrtdFYnpr0ZDHt8JOEVlvbvwnYjScicOXjLxyvfY4AA+q0xccIU0EX05JM2kc1BATDCxIpD8QrTIa2CjeOwGvaI60h/4I32xqFMnkxhbmDPoNeAmJVSR0EOouvtMMeePGMtb6VPZuykmNFHK2FMt1iFwGFUPRogRn4yBj0uFb9n8M8K4adadKzL1rvGIlMJHAI7arEYoGIv3f8QzwkwipnEyX1Vvq86HCaVRJkQXGbwYLioOJeL+t4bp9UpTzOhqdoI4ixDXfJ81sMnIG/UVp0Sq9pKARdRnVtclgJeUnBMJhnUmpsHyMsSc6I5dYuneDO6n',
    'baby-isWide': 'wide',
    'overrideAbTestGroup': '%5B%5D',
    'bm_ss': 'ab8e18ef4e',
    'web-session-id': '6895124a-faed-4696-93dd-96ba9c49c8b3',
    'bm_s': 'YAAQB9ojF8VjIkOXAQAA/HL7VwMPhjOuY89lYWzlKxH2238L3GQTcNVuECteMgciFdFMYwUbDUALSbu8s3A9Vo00kvkG5PPpeex0vksAnQdjDncmVsYSStFMDnf6jQTPpsmb5I3YdkXkObnXOkKV8DsFDZO6chDOcZLtR3Ttu55hqdOAlxXBAyorrkQi5/lXLpGZ0dXjImrNP5wdWhuffi7BlOp6DOcOBOZejLn4DuiVp9Wr1LKyI7MmqckbPDy7IGDnSDqBU3cP7yLvfiBTVHU4CIIFIfeXZ1X1NdCo3Au6uTLFIdfRB/PInK8ZIElDhVke3XyQFwawCYK9XS+0tA1cx53d8MpA0lD5Sm7abRWUoIbPnv0nTDTrwMhSV2BAoVujseSqWohbwSvBpm/ycDE6Fg0CTjF/ej+e2no2ym9XlNzVlNZNS4Zu7JDmnmE6lA6vZJoZ3dN8vZ4L4dFOXDH7Z1l/kalFLSEeWTYQk7pldO7hWTZCnDOS8xC8YnZNc4dV/bxDb5KAZIaBY5Cj5J+CbKESHGo39QS5DTR5GNsHDEPneYIgEUgFQdqdDY95gOShgUGsHc82p/wQw4Ad',
    'bm_so': 'F3B84463E7DCB50D73F642EE4899B158D697A26F84EA0827ADE3CE923A08C050~YAAQB9ojF8ZjIkOXAQAA/HL7VwO8wP8MYv/vUHQ81iDiK/bHSgiqI5EtUn25WH0krvBYY2KbXT2iOKQP9qUt2g8ftem9eGv7JVUnqn1OdBH3XEsNnkZOmZd/kBMvKweTlqzVGdIO/nrfS+bE7XFRY/MxTla1h7Mi0CrcGiu6r67ZDxoj3jtbYSot/iHkWATAg/bPtxD/P10iGLH228JkUZfqdW9gP6foK/J/iqyTcgRUMm27J+nTw2DMSV9w4Syv6PfU1efB8aqZmsD3HJSAfrcLchZCO/+rMZ/7ce1HQ7M4PbiPj4wriwF13WuzLGouOKU+dDwYOgExWtmoiGXbxhA1IM+HAo5rPMns3AD3fPgZS3Df8Fj7xH3Byx+EfYYiQDVXQSCsuSP+s7npC8FIzd4CDhm+gh2OBaJnbKoGIr/YtUjb1DoYq/w8SkmDpHi4Do/03vPIfZ1t/nG0uWxAUzM=',
    'bm_sz': '440F1BDFA4E691869DE7D49A30E7E13C~YAAQB9ojF8hjIkOXAQAA/HL7Vxx7N7D6y4PaMvK5x3UNfPpAdkSPxz9fn17Djta99xU0+o9SoSZTz3WUHidLA3ROBpJQwl2jQezKACN6JuHCtRQYvpTcPfFyDtZeFKcjZSp9m8cKE1g92fyo14ns1WTt26lr3YkHlAmUVhPlFe6F5PngqXj/sdrw41cM8VAGO7QiIuqu0bMwGeS9zby/hiEh8bN9z7aKFLkafpAXuBEoCG6sY75I/YdOGDo2WF8xsb7JSa+TzDXV3F+86OAHbo8V4LZZgrduFRJFIzBFVaP+a6xE1fmWg5Y7lCl+aRKr3DO24A6LXyj6PuPD+uEp8iVBqhzLjilOPGDss+feYayl0qRpSXCaMOPRBVykIPTMb53fYyfALb4w3VTxcKoI0PnJk7J/SQOYWgtUFEubl7AONngxuUuxUe70bLv/WpfNcMlDN0yT9ZIzszB3t9DPdA0zokkbtdUCqRGD1PLEktdalQ==~3359797~4339010',
    'bm_lso': 'F3B84463E7DCB50D73F642EE4899B158D697A26F84EA0827ADE3CE923A08C050~YAAQB9ojF8ZjIkOXAQAA/HL7VwO8wP8MYv/vUHQ81iDiK/bHSgiqI5EtUn25WH0krvBYY2KbXT2iOKQP9qUt2g8ftem9eGv7JVUnqn1OdBH3XEsNnkZOmZd/kBMvKweTlqzVGdIO/nrfS+bE7XFRY/MxTla1h7Mi0CrcGiu6r67ZDxoj3jtbYSot/iHkWATAg/bPtxD/P10iGLH228JkUZfqdW9gP6foK/J/iqyTcgRUMm27J+nTw2DMSV9w4Syv6PfU1efB8aqZmsD3HJSAfrcLchZCO/+rMZ/7ce1HQ7M4PbiPj4wriwF13WuzLGouOKU+dDwYOgExWtmoiGXbxhA1IM+HAo5rPMns3AD3fPgZS3Df8Fj7xH3Byx+EfYYiQDVXQSCsuSP+s7npC8FIzd4CDhm+gh2OBaJnbKoGIr/YtUjb1DoYq/w8SkmDpHi4Do/03vPIfZ1t/nG0uWxAUzM=^1749527788750',
    'bm_sv': '9969B64077D008A2F09237C7E5F83ADB~YAAQfYj+ecayTDuXAQAAofX7VxwSX8AyE86OTYMU5WldPt5LXkr83XN5r+BH2qw2/kHtjS+BaGi5raqDwcAh3y25hz+TqDNeThki55gXC+4y/fdLnQYT16QloSZzyrdys5Ab22qTzc7AhwyX61k/4H6l2obS6usZzaXM/AbATVIc5dAxeGMnK0J3Amt9PXXhXjL9o1nySiWEB9nuD/39w+oMnc1ax6oaSc1erpEyhcDvTgtAbl2p/dQDxpGp8n9Km68=~1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko,ko-KR;q=0.9,en;q=0.8',
    'baggage': 'sentry-environment=prod,sentry-release=prod-b3d20012b8a85b493001d628d5210e3c9f58e764,sentry-public_key=501af6039762e82f24831a3f1f892f3e,sentry-trace_id=ea43be2f9fe43d9e187becdbfbba06f8,sentry-sampled=false,sentry-sample_rand=0.24115215171649318,sentry-sample_rate=0',
    'priority': 'u=1, i',
    'referer': 'https://www.coupang.com/vp/products/1703093047?vendorItemId=70887318328&sourceType=HOME_RELATED_ADS&searchId=feed-ac023547d7d048748fc0d984becd3dc7-related_ads&clickEventId=96704670-45ab-11f0-b47f-6abd7cd42abf',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'ea43be2f9fe43d9e187becdbfbba06f8-87922f63d0221bdd-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    # 'cookie': 'PCID=16247705314370002565497; MARKETID=16247705314370002565497; x-coupang-accept-language=ko-KR; _fbp=fb.1.1739079230308.913915237482103068; gd1=Y; srp_delivery_toggle=true; delivery_toggle=false; x-coupang-target-market=KR; sid=8d4ed3a2517f4473b8e97d53bc2f25284379b851; searchKeyword=%EC%95%84%EC%9D%B4%ED%8F%B0%2015|%EC%95%84%EC%9D%B4%ED%8F%B015; searchKeywordType={%22%EC%95%84%EC%9D%B4%ED%8F%B0%2015%22:0}|{%22%EC%95%84%EC%9D%B4%ED%8F%B015%22:0}; trac_src=1042016; trac_spec=10304903; trac_addtag=900; trac_ctag=HOME; trac_lptag=%EC%BF%A0%ED%8C%A1; trac_itime=20250610111420; bm_mi=B656D513F9B392973C8C0115DB8F5571~YAAQB9ojF9Wb1EKXAQAA2xSeVxwGC+qiTmMDyaHWlMhf8sA77a+62ty/6Mg2CGatqDuGRAP4+Hx9EEeZS4Tx3ZSkK2EnPe8iVaoxjbIPa4CvmTsP5O4UqLZHEn/MjfNUkD7vXjl1NQN5ZuHw78qM4tVMKgaa+dk3bS3sNZYZWT0kfy8txCIdXMoct4BkBa+1/ia3WRNbKjmfTB18os3/V+o/rq7QAmNQ3OAlzaDgHAqjakGIPYXgNFK7eoVR68S3ZiTkPHXzISV5PxY6QkjKljEkeMMoDypMwrIahtbuKnr/PJIsxZEA5KZEr3XtSmyDNvB8vq6cCqUflNoTO6uZt2Uwyg==~1; _abck=59D6E61C9FC8339D97112BB1FC3EEAD5~0~YAAQB9ojF5ic1EKXAQAAzxWeVw4yS6HewzqGRRQLyrlu8rq87QzUDW3MJ3hGwqS2/rDSz4FbBGlY4NijNJgBXfIq2hkVol8qF04dRoLCicsDC5TwHp4lMCogSfnyvB1BArSxyQbwRh4roiCcxNQnFXKoVgY9ov3wk/9cW71x5o8hUxTlZXeOfZNUGSbD72v3NACJTpYqTw6SGC+HUUGuNa9Ph00L6ZmfY2CAWvscxSQcOxn8ej1dMeLB+fz0LCyp05cX3SAmvdbDj3hK2MjP3g/Vj1jOqNMAd5ZnsmX54zsb2P2G7ImLD9s3EayqkQXBT/5fLnovjj7nsFD0Dja5SbY8c/eMZoVpbR4kg5O5wGJTs7gpkrlMho+KEkW5FX8XVC14gnLYSkeq4Mgx2GEBxh6Hs0z3SZL95B+CDok/wsHLULtnfD+vliELkh4NXjVbFpAwh53mOaaFRsYuvujJ01yLxqmxwAkO3dyW8Deu/I+wm0tFGNH+M1aj5LkADzxj7KkzhYXYsBuTLVNh0DPmB8Uck22Y3xLvRRs2Bg9W68+8zKxTpiqp79czYtTw9L3jDWre2VHQ9hjB6DJsC3BJhysxfgDg2VUO7RH9rGk21hEQ4fzJJ3i3u8felG6WKO+F60rnnCfya0ThT9sB4ERuc+JYGz7utB8rK5BR++fvcM54znegWMGl6KnzflGE0zVE7J687iVWMyLO8tQBVFX1Kf6/mF7bSMZ8QfyY4y9wk0WfEgvRiDO0K5M4+EEguktZmRY=~-1~-1~1749024683; cto_bundle=CFmrv19hdzlqRzJkdE5RN09uOW1Vb2wzRTMzbWNaMVNUQTZUdzQyamFkSCUyRjdzOUZqVlY4VWF3cllCamtQeVE0UWQ0JTJGb1VXV2dHQ1dMSjc5bHVSc3l2VnRPdzc1R00lMkIlMkZaaERYd3VzQ3NlVkNxUSUyRmtFMEd4R3VHRTlTdTdOTFVMWmpuOXZ4bWV6VzdQaUElMkYxTDNmQyUyRkNza2VqMkF6OHZWSEgwMjJUUzNuNVZiMGptdVpTNlZOT2JVMFZsdHpKQ25qdnF6U0pNMUMlMkJnU0ZCV3ZUdTRmYiUyQk93RVVBJTNEJTNE; ak_bmsc=1BE11C51B47202E229EDDFD36D15FF68~000000000000000000000000000000~YAAQB9ojF9qr1EKXAQAANCmeVxwiL3oqcDIWTP8n2fSJjaBa/6/bDU+Mp8eVbwipnCXCOtLanVAlAog958fFn/lNm2P+wRMOSo5uUHo/ZlJBQy2a7aQjFQAk+0FuR0ntyKyr3BisBPyTAE83L3zZSFp/MvMW24WHROQAoiosIGbTvFJTsYnLrQoWmny4JkkxD4dLcrtdFYnpr0ZDHt8JOEVlvbvwnYjScicOXjLxyvfY4AA+q0xccIU0EX05JM2kc1BATDCxIpD8QrTIa2CjeOwGvaI60h/4I32xqFMnkxhbmDPoNeAmJVSR0EOouvtMMeePGMtb6VPZuykmNFHK2FMt1iFwGFUPRogRn4yBj0uFb9n8M8K4adadKzL1rvGIlMJHAI7arEYoGIv3f8QzwkwipnEyX1Vvq86HCaVRJkQXGbwYLioOJeL+t4bp9UpTzOhqdoI4ixDXfJ81sMnIG/UVp0Sq9pKARdRnVtclgJeUnBMJhnUmpsHyMsSc6I5dYuneDO6n; baby-isWide=wide; overrideAbTestGroup=%5B%5D; bm_ss=ab8e18ef4e; web-session-id=6895124a-faed-4696-93dd-96ba9c49c8b3; bm_s=YAAQB9ojF8VjIkOXAQAA/HL7VwMPhjOuY89lYWzlKxH2238L3GQTcNVuECteMgciFdFMYwUbDUALSbu8s3A9Vo00kvkG5PPpeex0vksAnQdjDncmVsYSStFMDnf6jQTPpsmb5I3YdkXkObnXOkKV8DsFDZO6chDOcZLtR3Ttu55hqdOAlxXBAyorrkQi5/lXLpGZ0dXjImrNP5wdWhuffi7BlOp6DOcOBOZejLn4DuiVp9Wr1LKyI7MmqckbPDy7IGDnSDqBU3cP7yLvfiBTVHU4CIIFIfeXZ1X1NdCo3Au6uTLFIdfRB/PInK8ZIElDhVke3XyQFwawCYK9XS+0tA1cx53d8MpA0lD5Sm7abRWUoIbPnv0nTDTrwMhSV2BAoVujseSqWohbwSvBpm/ycDE6Fg0CTjF/ej+e2no2ym9XlNzVlNZNS4Zu7JDmnmE6lA6vZJoZ3dN8vZ4L4dFOXDH7Z1l/kalFLSEeWTYQk7pldO7hWTZCnDOS8xC8YnZNc4dV/bxDb5KAZIaBY5Cj5J+CbKESHGo39QS5DTR5GNsHDEPneYIgEUgFQdqdDY95gOShgUGsHc82p/wQw4Ad; bm_so=F3B84463E7DCB50D73F642EE4899B158D697A26F84EA0827ADE3CE923A08C050~YAAQB9ojF8ZjIkOXAQAA/HL7VwO8wP8MYv/vUHQ81iDiK/bHSgiqI5EtUn25WH0krvBYY2KbXT2iOKQP9qUt2g8ftem9eGv7JVUnqn1OdBH3XEsNnkZOmZd/kBMvKweTlqzVGdIO/nrfS+bE7XFRY/MxTla1h7Mi0CrcGiu6r67ZDxoj3jtbYSot/iHkWATAg/bPtxD/P10iGLH228JkUZfqdW9gP6foK/J/iqyTcgRUMm27J+nTw2DMSV9w4Syv6PfU1efB8aqZmsD3HJSAfrcLchZCO/+rMZ/7ce1HQ7M4PbiPj4wriwF13WuzLGouOKU+dDwYOgExWtmoiGXbxhA1IM+HAo5rPMns3AD3fPgZS3Df8Fj7xH3Byx+EfYYiQDVXQSCsuSP+s7npC8FIzd4CDhm+gh2OBaJnbKoGIr/YtUjb1DoYq/w8SkmDpHi4Do/03vPIfZ1t/nG0uWxAUzM=; bm_sz=440F1BDFA4E691869DE7D49A30E7E13C~YAAQB9ojF8hjIkOXAQAA/HL7Vxx7N7D6y4PaMvK5x3UNfPpAdkSPxz9fn17Djta99xU0+o9SoSZTz3WUHidLA3ROBpJQwl2jQezKACN6JuHCtRQYvpTcPfFyDtZeFKcjZSp9m8cKE1g92fyo14ns1WTt26lr3YkHlAmUVhPlFe6F5PngqXj/sdrw41cM8VAGO7QiIuqu0bMwGeS9zby/hiEh8bN9z7aKFLkafpAXuBEoCG6sY75I/YdOGDo2WF8xsb7JSa+TzDXV3F+86OAHbo8V4LZZgrduFRJFIzBFVaP+a6xE1fmWg5Y7lCl+aRKr3DO24A6LXyj6PuPD+uEp8iVBqhzLjilOPGDss+feYayl0qRpSXCaMOPRBVykIPTMb53fYyfALb4w3VTxcKoI0PnJk7J/SQOYWgtUFEubl7AONngxuUuxUe70bLv/WpfNcMlDN0yT9ZIzszB3t9DPdA0zokkbtdUCqRGD1PLEktdalQ==~3359797~4339010; bm_lso=F3B84463E7DCB50D73F642EE4899B158D697A26F84EA0827ADE3CE923A08C050~YAAQB9ojF8ZjIkOXAQAA/HL7VwO8wP8MYv/vUHQ81iDiK/bHSgiqI5EtUn25WH0krvBYY2KbXT2iOKQP9qUt2g8ftem9eGv7JVUnqn1OdBH3XEsNnkZOmZd/kBMvKweTlqzVGdIO/nrfS+bE7XFRY/MxTla1h7Mi0CrcGiu6r67ZDxoj3jtbYSot/iHkWATAg/bPtxD/P10iGLH228JkUZfqdW9gP6foK/J/iqyTcgRUMm27J+nTw2DMSV9w4Syv6PfU1efB8aqZmsD3HJSAfrcLchZCO/+rMZ/7ce1HQ7M4PbiPj4wriwF13WuzLGouOKU+dDwYOgExWtmoiGXbxhA1IM+HAo5rPMns3AD3fPgZS3Df8Fj7xH3Byx+EfYYiQDVXQSCsuSP+s7npC8FIzd4CDhm+gh2OBaJnbKoGIr/YtUjb1DoYq/w8SkmDpHi4Do/03vPIfZ1t/nG0uWxAUzM=^1749527788750; bm_sv=9969B64077D008A2F09237C7E5F83ADB~YAAQfYj+ecayTDuXAQAAofX7VxwSX8AyE86OTYMU5WldPt5LXkr83XN5r+BH2qw2/kHtjS+BaGi5raqDwcAh3y25hz+TqDNeThki55gXC+4y/fdLnQYT16QloSZzyrdys5Ab22qTzc7AhwyX61k/4H6l2obS6usZzaXM/AbATVIc5dAxeGMnK0J3Amt9PXXhXjL9o1nySiWEB9nuD/39w+oMnc1ax6oaSc1erpEyhcDvTgtAbl2p/dQDxpGp8n9Km68=~1',
}

params = {
    'productId': '1703093047',
    'page': '2',
    'size': '10',
    'sortBy': 'ORDER_SCORE_ASC',
    'ratingSummary': 'true',
    'ratings': '',
    'market': '',
}



response = requests.get('https://www.coupang.com/next-api/review', params=params, cookies=cookies, headers=headers)
data = json.loads(response.text)

# print(data['rData']['paging']['contents'])

dataList = []

dataReview = data['rData']['paging']['contents']
totalCount = data['rData']['paging']['totalCount']




for k in range(1,10):
    params['page'] = k
    response = requests.get('https://www.coupang.com/next-api/review', params=params, cookies=cookies, headers=headers)
    data = json.loads(response.text)
    dataReview = data['rData']['paging']['contents']
    
    for i in dataReview:
        # dataList.append(
        #     i['reviewId']
        # )
        dataList.append(
            {
                'reviewId': i['reviewId'],
                'content':i['content']
            }
        )



print(dataList)




