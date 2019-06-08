# Setup
pip install -r requirement.txt`
# Preprocessing
split the news tilte in to four classes and save them in to 4 separate text file  like,

        1. Head Infotech invests $1 Mn to acquire majority stake in startup FanFight (belongs to funding category)
        2. After Alibaba and Tencent, Softbank eyes to invest $200-250 Mn in Swiggy  (belongs to funding category)

        3. Amazon Pay scoops up Rs 195 Cr from parent entity, appoints Mahendra Nerurkar as director  (belongs to hiring category)
        4. Paytm eyes 500 Mn users in two years,  hire 10,000 workers for KYC (belongs to hiring category)

        5. Xiaomi launches UPI-powered Mi Pay in beta   (belongs to new_offering category)
        6. Google launches mobile data manager app Datally in India  (belongs to new_offering category)

        7. OYO acquires midscale Chinese hotel brand Qianyu (belongs to acquire category)
        8. Walmart acquires 77% of Flipkart for $16 Bn (belongs to acquire category)

modify the config.json
        1. add paths of created text file(like funding.txt,hiring.txt,new_offering.txt,acquire.txt)

# To Run
python preprocessing.py
python RelExt.py   
# TO Predict
modify predict.py
add your text in following line
sentence = Sentence('add your text here for prediction')
save

python predict.py