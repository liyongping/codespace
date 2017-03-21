# -*- coding: utf-8 -*-

'''
Download corresponding materials' pdf file from 121talk.com
'''

import os
import urllib2
from bs4 import BeautifulSoup


base_url = "http://class.yeko.org.cn/Public/Uploads/Materials/"

select_str = '<select class="mid" name="mt_id">\
<option value="1015419" pdf="5732c6ff94de1.pdf">Conversation 1 Are business lunch 商务午餐</option>\
<option value="1015420" pdf="5732c71d0d1d4.pdf">Conversation 2 Casual conversion 商务话题随意聊</option>\
<option value="1015421" pdf="5732c7308d00f.pdf">Conversation 3 Congratulating a Client 祝贺客户</option>\
<option value="1015422" pdf="5732c74a051ce.pdf">Conversation 4 Stealing clients away 撬走客户</option>\
<option value="1015423" pdf="5732c76b7068e.pdf">Conversation 5 Advising clients 给客户提建议</option>\
<option value="1015424" pdf="5732c78d9ac96.pdf">Conversation 6 A second option 说出你的想法</option>\
<option value="1015425" pdf="5732c7c7e6f17.pdf">Conversation 7 Talking your company up 说出公司优势</option>\
<option value="1015426" pdf="5732c7dc9f5e5.pdf">Conversation 8 Coming at the opinion from all angles 想法要周全</option>\
<option value="1015427" pdf="5732c7f70d616.pdf">Conversation 9 Confirming an order 确定订单</option>\
<option value="1015428" pdf="5732c80c6055d.pdf">Conversation 10 Finalizing an order 完成订单</option>\
<option value="1015429" pdf="5732c82142555.pdf">Conversation 11 Extending credit to clients 向客户提供信用贷款</option>\
<option value="1015430" pdf="5732c8354e629.pdf">Conversation 12 Offering chances to clients 给客户提供机会</option>\
<option value="1015431" pdf="5732c84aa1199.pdf">Conversation 13 Handling complaints 处理客户投诉</option>\
<option value="1015432" pdf="5732c862e325d.pdf">Conversation 14 Individualized service 个性化服务</option>\
<option value="1015433" pdf="5732c87816015.pdf">Conversation 15 Investing money for clients 为客户做投资</option>\
<option value="1015434" pdf="5732c88b0ed64.pdf">Conversation 16 Your reputation precedes you 久仰贵公司大名</option>\
<option value="1015435" pdf="5732c89f0c7ea.pdf">Conversation 17 Getting through tough times together 共度难关</option>\
<option value="1015436" pdf="5732c8b896d83.pdf">Conversation 18 Putting your best foot forward 展示最好的形象</option>\
<option value="1015437" pdf="5732c8cef04ad.pdf">Conversation 19 Clients can count on you 信任至上</option>\
<option value="1015438" pdf="5732c8e4e8a6d.pdf">Conversation 20 The customer is always right 客户永远是对的</option>\
<option value="1015439" pdf="5732c9030abf7.pdf">Conversation 21 Troubleshooting with clients 为客户排除故障</option>\
<option value="1015440" pdf="5732c91ecf260.pdf">Conversation 22 Polite communication 礼貌沟通</option>\
<option value="1015441" pdf="5732c931c6e92.pdf">Conversation 23 Winning clients back 重新赢得客户</option>\
<option value="1015442" pdf="5732c95cee0f9.pdf">Conversation 24 Success comes to those that earn it 成功来自努力</option>\
<option value="1015443" pdf="5732c96e2362c.pdf">Conversation 25 The key to success is good timing 选好时机是成功关键</option>\
<option value="1015444" pdf="5732c97fa700d.pdf">Conversation 26 Financial troubles 财务困难</option>\
<option value="1015445" pdf="5732c99c5492d.pdf">Conversation 27 We\'re in the red 我们在负债</option>\
<option value="1015446" pdf="5732c9af26b33.pdf">Conversation 28 A company in dire financial straits 在艰难境地中</option>\
<option value="1015447" pdf="5732c9bee1b80.pdf">Conversation 29 Generating revenue 创收</option>\
<option value="1015448" pdf="5732c9d1e2800.pdf">Conversation 30 Personnel changes 人事变动</option>\
<option value="1015449" pdf="5732c9e3aa590.pdf">Conversation 31 Quarterly evaluations 季度评估</option>\
<option value="1015450" pdf="5732c9f84cf4c.pdf">Conversation 32 Submitting one\'s resignation 递交辞职信</option>\
<option value="1015451" pdf="5732ca137d423.pdf">Conversation 33 I need to take a few days off 请事假</option>\
<option value="1015452" pdf="5732ca2770faf.pdf">Conversation 34 I need a vacation 休假</option>\
<option value="1015453" pdf="5732ca3a914d2.pdf">Conversation 35 Maternity leave 休产假</option>\
<option value="1015454" pdf="5732ca4d5798e.pdf">Conversation 36 Self-introduction 自我介绍</option>\
<option value="1015455" pdf="5732ca68c7a1e.pdf">Conversation 37 Expressing your greatest strength 说明你的优点</option>\
<option value="1015456" pdf="5732ca7965153.pdf">Conversation 38 Working philosophy 说明工作理念</option>\
<option value="1015457" pdf="5732ca8b5bb7e.pdf">Conversation 39 The employment contract 讨论劳动合同</option>\
<option value="1015458" pdf="5732ca9fb01cb.pdf">Conversation 40 Renewing a contract 续签合同</option>\
<option value="1015459" pdf="5732cab08ff2a.pdf">Conversation 41 Bonuses 奖金</option><option value="1015460" pdf="5732cac425cc7.pdf">Conversation 42 Pay day 发薪日</option><option value="1015461" pdf="5732cad790ec3.pdf">Conversation 43 Tax withheld 扣税</option><option value="1015462" pdf="5732cae9a1eeb.pdf">Conversation 44 Taking on more responsibilities 我愿承担更多的责任</option><option value="1015463" pdf="5732cafa5f5a5.pdf">Conversation 45 Facing an internal opening 面对职位空缺</option><option value="1015464" pdf="5732cb0c6be00.pdf">Conversation 46 Technological training 技术培训</option><option value="1015465" pdf="5732cb1fa32c5.pdf">Conversation 47 Diversity training 多元化工作环境培训</option><option value="1015466" pdf="5732cb30b3569.pdf">Conversation 48 New procedures training 新程序培训</option><option value="1015467" pdf="5732cb42ddbaf.pdf">Conversation 49 A company retreat 野外拓展活动</option><option value="1015468" pdf="5732cb59049fc.pdf">Conversation 50 Confirming design plans 确定设计方案</option><option value="1015469" pdf="5732cbe662e2c.pdf">Conversation 51 Nothing ventured，nothing gained 不入虎穴，焉得虎子</option><option value="1015470" pdf="5732cbfd9255a.pdf">Conversation 52 Not an all-or-nothing proposition 这是个中肯的提议</option><option value="1015471" pdf="5732cc0fef33c.pdf">Conversation 53 You really think outside the box 你太有创意了！</option><option value="1015472" pdf="5732cc228f4c1.pdf">Conversation 54 Marketing campaigns 营销活动</option><option value="1015473" pdf="5732cc3434223.pdf">Conversation 55 Advertisement online 网络广告</option><option value="1015474" pdf="5732cc49d559b.pdf">Conversation 56 Brainstorming 集思广益</option><option value="1015475" pdf="5732cca16b63d.pdf">Conversation 57 Maintaining growth 保持增长</option><option value="1015476" pdf="5732ccb230d78.pdf">Conversation 58 Direction of the market 市场发展趋势</option><option value="1015477" pdf="5732ccc3e9944.pdf">Conversation 59 Making reasonable projections 合理预测</option><option value="1015478" pdf="5732ccd661420.pdf">Conversation 60 Projections of unexpected costs 预算外支出</option><option value="1015479" pdf="5732cce90f5a0.pdf">Conversation 61 Friction between co-workers 同事间摩擦</option><option value="1015480" pdf="5732ccfbb86e8.pdf">Conversation 62 A simple misunderstanding 只是一点儿小误会</option><option value="1015481" pdf="5732cd0fdd54e.pdf">Conversation 63 Conflict management 冲突管理</option><option value="1015482" pdf="5732cd258c938.pdf">Conversation 64 Getting reimbursed 报销</option><option value="1015483" pdf="5732cd3ab196a.pdf">Conversation 65 Paperwork 文书工作</option><option value="1015484" pdf="5732cd4c5a8bb.pdf">Conversation 66 The big picture 公司的整体情况</option><option value="1015485" pdf="5732cd63bdd86.pdf">Conversation 67 Don\'t bite off more than you can chew请勿好高骛远</option><option value="1015486" pdf="5732cd78d3690.pdf">Conversation 68 A bird in the hand is worth two in the bush宁可求稳，也别出错</option><option value="1015487" pdf="5732cd8d36c77.pdf">Conversation 69 Everything is going according to plan一切都在按计划进行吗？</option><option value="1015488" pdf="5732cd9fddc80.pdf">Conversation 70 Staying ahead of schedule 提前完成计划</option><option value="1015489" pdf="5732cdb530874.pdf">Conversation 71 Sharing project responsibilities分担项目责任</option><option value="1015490" pdf="5732cdcc9558b.pdf">Conversation 72 Two heads are better than one三个臭皮匠，赛过诸葛亮</option><option value="1015491" pdf="5732cde1777d8.pdf">Conversation 73 Teamwork 团队合作</option><option value="1015492" pdf="5732cdf3c2fc4.pdf">Conversation 74 Timelines 时间表</option><option value="1015493" pdf="5732ce072c832.pdf">Conversation 75 The process was hold up 项目进展受阻</option><option value="1015494" pdf="5732ce21a6fa4.pdf">Conversation 76 Annual meeting 公司年会</option><option value="1015495" pdf="5732cea685def.pdf">Conversation 77 We\'ve had a bad year 今年业绩不好</option><option value="1015496" pdf="5732cebc41952.pdf">Conversation 78 Cancelling a meeting 取消会议</option><option value="1015497" pdf="5732cece0a89f.pdf">Conversation 79 Department meeting 部门会议</option><option value="1015498" pdf="5732cf65114f9.pdf">Conversation 80 Monthly meeting 每月例会</option><option value="1015499" pdf="5732cf89f311c.pdf">Conversation 81 Question and answer session 会议问答阶段</option><option value="1015500" pdf="5732cf9d4bb95.pdf">Conversation 82 Scheduling a meeting 安排会面</option><option value="1015501" pdf="5732d0b6ee888.pdf">Conversation 83 Rescheduling a meeting 重新安排会面</option><option value="1015502" pdf="5732d0f74f608.pdf">Conversation 84 Finalizing the terms of the contract 确定合同条款</option><option value="1015503" pdf="5732d109b8c4d.pdf">Conversation 85 Reading the fine print 阅读合同细则</option><option value="1015504" pdf="5732d12217dd6.pdf">Conversation 86 Contracts are the final word 遵照合同办事</option><option value="1015505" pdf="5732d15e14609.pdf">Conversation 87 Delivering an ultimatum 下最后通牒</option><option value="1015506" pdf="5732d1a70bd1c.pdf">Conversation 88 Negotiating with clients 与客户谈判</option><option value="1015507" pdf="5732d1ed09226.pdf">Conversation 89 Not a penny less 讨价还价</option><option value="1015508" pdf="5732d28db42d8.pdf">Conversation 90 Renegotiate existing agreements 重新协商条款</option><option value="1015509" pdf="5732d2c99dd64.pdf">Conversation 91 Re-evaluations of contract terms 重新评估条款</option><option value="1015510" pdf="5732d2f26d86a.pdf">Conversation 92 A joint venture 合营企业</option><option value="1015511" pdf="5732d305a1e57.pdf">Conversation 93 Hostile takeovers 恶意接管</option><option value="1015512" pdf="5732d34b1a427.pdf">Conversation 94 Mergersacquisitionsand takeovers 兼并，收购和接管</option><option value="1015513" pdf="5732d35bb35df.pdf">Conversation 95 Keep up the good work 继续努力，好好干吧！</option><option value="1015514" pdf="5732d378d6ed0.pdf">Conversation 96 You have a lot of potential 你很有潜力</option><option value="1015515" pdf="5732d38ab806a.pdf">Conversation 97 This really made my day 这会让我高兴一整天</option><option value="1015516" pdf="5732d39ca104b.pdf">Conversation 98 At an exhibition 在展览会上</option><option value="1015517" pdf="5732d3e299ccb.pdf">Conversation 99 Attending a business conference 参加商务会议</option><option value="1015518" pdf="5732d406eef19.pdf">Conversation 100 Attending an awards ceremony 参加颁奖典礼</option></select>'

# setup proxy
proxy = urllib2.ProxyHandler({'http': 'cn-proxy.jp.oracle.com:80'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

directory = "output"
if not os.path.exists(directory):
    os.makedirs(directory)


ptag = BeautifulSoup(select_str)
for option in ptag.find_all('option'):
    class_name =  option.get_text()

    pdf_url = base_url + option["pdf"]

    # set the encode "gb2312" to print correct chinese name in cmd
    print "Download: " + class_name.encode('gb2312'), "url: " + pdf_url,

    #download the corresponding pdf file as class pdf file
    pdf_file = urllib2.urlopen(pdf_url)
    with open(os.path.join(directory, class_name + '.pdf'), 'wb') as output:
        output.write(pdf_file.read())
    print " Done"