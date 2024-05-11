import keywords_classify as kc
text='VPN reimplementation because of netmask change. We must extend our subnet. In the future we will use other address to access servers. So we must reconfigure. After change we will switch of  the Juniper router'
text_classes = kc.classify_text(text)
print(text_classes)
new_class_name = kc.max_class(text_classes) if text_classes else 'DEV'
print(new_class_name)