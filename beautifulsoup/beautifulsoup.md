# 爬蟲練習
## 工具
1.  python3.8
2.  [requests]() ==> 負責抓取檔案
3.  [beautifulsoup](https://web.archive.org/web/20170127002045/https://www.crummy.com/software/BeautifulSoup/bs4/doc/) ==> 負責分析requests抓下來的檔案
## 安裝
```
pip install beautifulsoup
```

'''
pip install requests
'''
## 實作
#### 抓取網站內容
以gooele為例

request.get() ==> download the web's html

BeautifulSoup(news.text,'html.parser') ==> analysis the html code,and build the object

'''
from bs4 import BeautifulSoup
import requests
news=requests.get('https://www.google.com/')
soup=BeautifulSoup(news.text,'html.parser')

#output the html content
print(soup.prettify())
'''
#### 抓取網站內容結果
'''
<!DOCTYPE html>
<html itemscope="" itemtype="http://schema.org/WebPage" lang="zh-TW">
 <head>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  <meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"/>
  <title>
   Google
  </title>
  <script nonce="f60DObb2leOZj5nmLKq2ow==">
   (function(){window.google={kEI:'uDwHYumPD5WImgbQrovwCQ',kEXPI:'0,1302536,56873,6058,207,4804,921,1395,383,246,5,1354,4013,1237,1122516,1197753,648,30,380060,16114,17444,11240,17572,4858,1362,9291,3023,2821,14764,4998,13228,3847,4192,6431,22742,5079,887,707,1278,2743,148,1103,840,1983,214,4100,108,3406,606,2023,1777,520,14670,3227,2845,7,5599,11851,16320,908,2,941,2614,13142,3,576,4385,2075,148,12314,1661,4,1527,656,1649,11722,204,20186,2658,6701,656,30,13628,2305,2132,16786,5827,2530,4094,17,4035,3,3541,1,16807,38,6866,18443,2,14022,1931,5589,743,5853,9326,1137,1160,3481,2198,1020,2378,2721,18297,2,6,7718,4568,2578,2788,890,3005,3,3712,10729,1182,4790,830,422,5835,13829,1138,2850,1483,20,4996,1016,58,1394,445,2,2,1,1509,4154,5126,6839,2,1,6152,843,1559,10,1,436,285,395,2,781,6547,82,63,113,805,4206,5,37,5,294,101,71,944,638,161,1,131,56,2,1290,384,885,190,963,2715,4276,414,2621,3,749,2376,2803,364,31,976,341,451,9,2,354,48,40,512,1,433,716,100,286,716,493,910,640,46,2680,6,3,674,162,658,168,1616,206,424,432,61,52,245,6,5480097,2031,102,5996692,2801217,882,444,1,2,80,1,1797,2,7,2553,1,748,141,795,563,1,4265,1,1,2,1331,4142,2609,155,17,13,72,139,4,2,20,2,169,13,19,46,5,39,96,548,29,2,2,1,2,1,2,2,7,4,1,2,2,2,2,2,2,353,513,186,1,1,158,3,2,2,2,2,2,4,2,3,3,269,1601,141,348,43,3,178,10,5,48,3,2,4,7454293,16498044,4041689,3,450,1964,1491,9,1435,159,1358,4726,3,927,318,20,3196,97,386,565,682,74',kBL:'DwE_'};google.sn='webhp';google.kHL='zh-TW';})();(function(){
var f=this||self;var h,k=[];function l(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return 
b||h}function m(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b}
function n(a,b,c,d,g){var e="";c||-1!==b.search("&ei=")||(e="&ei="+l(d),-1===b.search("&lei=")&&(d=m(d))&&(e+="&lei="+d));d="";!c&&f._cshid&&-1===b.search("&cshid=")&&"slh"!==a&&(d="&cshid="+f._cshid);c=c||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+e+"&zx="+Date.now()+d;/^http:/i.test(c)&&"https:"===window.location.protocol&&(google.ml&&google.ml(Error("a"),!1,{src:c,glmm:1}),c="");return c};h=google.kEI;google.getEI=l;google.getLEI=m;google.ml=function(){return null};google.log=function(a,b,c,d,g){if(c=n(a,b,c,d,g)){a=new Image;var e=k.length;k[e]=a;a.onerror=a.onload=a.onabort=function(){delete k[e]};a.src=c}};google.logUrl=n;}).call(this);(function(){
google.y={};google.sy=[];google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.sx=function(a){google.sy.push(a)};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};google.bx=!1;google.lx=function(){};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"===c||"q"===c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!==document.documentElement;a=a.parentElement)if("A"===a.tagName){a="1"===a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);
  </script>
  <style>
   #gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
  </style>
  <style>
   body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#1558d6}em{color:#c5221f;font-style:normal;font-weight:normal}a em{text-decoration:underline}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#4b11a8;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#1558d6}a:visited{color:#4b11a8}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#f8f9fa;border:solid 1px;border-color:#dadce0 #70757a #70757a #dadce0;height:30px}.lsbb{display:block}#WqQANb a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#dadce0}.lst:focus{outline:none}
  </style>
  <script nonce="f60DObb2leOZj5nmLKq2ow==">
   (function(){window.google.erd={jsr:1,bv:1529,de:true};
var f=this||self;var g,h,k=null!==(g=f.mei)&&void 0!==g?g:1,l=null!==(h=f.sdo)&&void 0!==h?h:!0,p=0,q,r=google.erd,u=r.jsr;google.ml=function(a,b,d,m,c){c=void 0===c?2:c;b&&(q=a&&a.message);if(google.dl)return google.dl(a,c,d),null;if(0>u){window.console&&console.error(a,d);if(-2===u)throw a;b=!1}else b=!a||!a.message||"Error loading script"===a.message||p>=k&&!m?!1:!0;if(!b)return null;p++;d=d||{};var e=c;c=encodeURIComponent;b="/gen_204?atyp=i&ei="+c(google.kEI);google.kEXPI&&(b+="&jexpid="+c(google.kEXPI));b+="&srcpg="+c(google.sn)+"&jsr="+c(r.jsr)+"&bver="+c(r.bv)+("&jsel="+e);e=a.lineNumber;void 0!==e&&(b+="&line="+
e);var n=a.fileName;n&&(b+="&script="+c(n),e&&n===window.location.href&&(e=document.documentElement.outerHTML.split("\n")[e],b+="&cad="+c(e?e.substring(0,300):"No script found.")));for(var t in d)b+="&",b+=c(t),b+="=",b+=c(d[t]);b=b+"&emsg="+c(a.name+": "+a.message);b=b+"&jsst="+c(a.stack||"N/A");12288<=b.length&&(b=b.substr(0,12288));a=b;m||google.log(0,"",a);return a};window.onerror=function(a,b,d,m,c){q!==a&&(a=c instanceof Error?c:Error(a),void 0===d||"lineNumber"in a||(a.lineNumber=d),void 0===b||"fileName"in a||(a.fileName=b),google.ml(a,!1,void 0,!1,"SyntaxError"===a.name||"SyntaxError"===a.message.substring(0,11)?2:0));q=null;l&&p>=k&&(window.onerror=null)};})();
  </script>
 </head>
 <body bgcolor="#fff">
  <script nonce="f60DObb2leOZj5nmLKq2ow==">
   (function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if 
(document.images){new Image().src=src;}
if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}
}
})();
  </script>
  <div id="mngb">
   <div id="gbar">
    <nobr>
     <b class="gb1">
      搜尋
     </b>
     <a class="gb1" href="https://www.google.com.tw/imghp?hl=zh-TW&amp;tab=wi">
      圖片
     </a>
     <a class="gb1" href="https://maps.google.com.tw/maps?hl=zh-TW&amp;tab=wl">
      地圖
     </a>
     <a class="gb1" href="https://play.google.com/?hl=zh-TW&amp;tab=w8">
      Play
     </a>
     <a class="gb1" href="https://www.youtube.com/?gl=TW&amp;tab=w1">
      YouTube
     </a>
     <a class="gb1" href="https://news.google.com/?tab=wn">
      新聞
     </a>
     <a class="gb1" href="https://mail.google.com/mail/?tab=wm">
      Gmail
     </a>
     <a class="gb1" href="https://drive.google.com/?tab=wo">
      雲端硬碟
     </a>
     <a class="gb1" href="https://www.google.com.tw/intl/zh-TW/about/products?tab=wh" style="text-decoration:none">
      <u>
       更多
      </u>
      »
     </a>
    </nobr>
   </div>
   <div id="guser" width="100%">
    <nobr>
     <span class="gbi" id="gbn">
     </span>
     <span class="gbf" id="gbf">
     </span>
     <span id="gbe">
     </span>
     <a class="gb4" href="http://www.google.com.tw/history/optout?hl=zh-TW">
      網頁記錄
     </a>
     |
     <a class="gb4" href="/preferences?hl=zh-TW">
      設定
     </a>
     |
     <a class="gb4" href="https://accounts.google.com/ServiceLogin?hl=zh-TW&amp;passive=true&amp;continue=https://www.google.com/&amp;ec=GAZAAQ" id="gb_70" target="_top">
      登入
     </a>
    </nobr>
   </div>
   <div class="gbh" style="left:0">
   </div>
   <div class="gbh" style="right:0">
   </div>
  </div>
  <center>
   <br clear="all" id="lgpd"/>
   <div id="lga">
    <img alt="Google" height="92" id="hplogo" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272"/>
    <br/>
    <br/>
   </div>
   <form action="/search" name="f">
    <table cellpadding="0" cellspacing="0">
     <tr valign="top">
      <td width="25%">
      </td>
      <td align="center" nowrap="">
       <input name="ie" type="hidden" value="ISO-8859-1"/>
       <input name="hl" type="hidden" value="zh-TW"/>
       <input name="source" type="hidden" value="hp"/>
       <input name="biw" type="hidden"/>
       <input name="bih" type="hidden"/>
       <div class="ds" style="height:32px;margin:4px 0">
        <input autocomplete="off" class="lst" maxlength="2048" name="q" size="57" style="margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000" title="Google 搜尋" value=""/>
       </div>
       <br style="line-height:0"/>
       <span class="ds">
        <span class="lsbb">
         <input class="lsb" name="btnG" type="submit" value="Google 搜尋"/>
        </span>
       </span>
       <span class="ds">
        <span class="lsbb">
         <input class="lsb" id="tsuid1" name="btnI" type="submit" value="好手氣"/>
         <script nonce="f60DObb2leOZj5nmLKq2ow==">
          (function(){var id='tsuid1';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}
else top.location='/doodles/';};})();
         </script>
         <input name="iflsig" type="hidden" value="AHkkrS4AAAAAYgdKyOBeEDfrRhWJoFKiWMiNQIm1ArgY"/>
        </span>
       </span>
      </td>
      <td align="left" class="fl sblc" nowrap="" width="25%">
       <a href="/advanced_search?hl=zh-TW&amp;authuser=0">
        進階搜尋
       </a>
      </td>
     </tr>
    </table>
    <input id="gbv" name="gbv" type="hidden" value="1"/>
    <script nonce="f60DObb2leOZj5nmLKq2ow==">
     (function(){
var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);
    </script>
   </form>
   <div id="gac_scont">
   </div>
   <div style="font-size:83%;min-height:3.5em">
    <br/>
   </div>
   <span id="footer">
    <div style="font-size:10pt">
     <div id="WqQANb" style="margin:19px auto;text-align:center">
      <a href="http://www.google.com.tw/intl/zh-TW/services/">
       商業解決方案
      </a>
      <a href="/intl/zh-TW/about.html">
       關於 Google
      </a>
      <a href="https://www.google.com/setprefdomain?prefdom=TW&amp;prev=https://www.google.com.tw/&amp;sig=K_osIEkVzFbqEOi_F8yp7oYABIpB4%3D">
       Google.com.tw
      </a>
     </div>
    </div>
    <p style="font-size:8pt;color:#70757a">
     © 2022 -
     <a href="/intl/zh-TW/policies/privacy/">
      隱私權
     </a>
     -
     <a href="/intl/zh-TW/policies/terms/">
      服務條款
     </a>
    </p>
   </span>
  </center>
  <script nonce="f60DObb2leOZj5nmLKq2ow==">
   (function(){window.google.cdo={height:757,width:1440};(function(){
var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();
  </script>
  <script nonce="f60DObb2leOZj5nmLKq2ow==">
   (function(){google.xjs={ck:'',cs:'',excm:[]};})();
  </script>
  <script nonce="f60DObb2leOZj5nmLKq2ow==">
   (function(){var u='/xjs/_/js/k\x3dxjs.hp.en.syj10ODtUPY.O/am\x3dAPAEAEACkA/d\x3d1/ed\x3d1/esmo\x3d1/rs\x3dACT90oFONrrpSc0WzO0b108d-e5n8M0V6w/m\x3dsb_he,d';
var e=this||self,f=function(a){return a};var g;var l=function(a,b){this.g=b===h?a:""};l.prototype.toString=function(){return this.g+""};var h={};
function m(){var a=u;google.lx=function(){n(a);google.lx=function(){}};google.bx||google.lx()}
function n(a){google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");var b=document;var c="SCRIPT";"application/xhtml+xml"===b.contentType&&(c=c.toLowerCase());c=b.createElement(c);if(void 0===g){b=null;var k=e.trustedTypes;if(k&&k.createPolicy){try{b=k.createPolicy("goog#html",{createHTML:f,createScript:f,createScriptURL:f})}catch(p){e.console&&e.console.error(p.message)}g=b}else g=b}a=(b=g)?b.createScriptURL(a):a;a=new l(a,h);c.src=a instanceof l&&a.constructor===l?a.g:"type_error:TrustedResourceUrl";var d;a=(c.ownerDocument&&c.ownerDocument.defaultView||window).document;(d=(b=null===(d=a.querySelector)||void 0===d?void 0:d.call(a,"script[nonce]"))?b.nonce||b.getAttribute("nonce")||"":"")&&c.setAttribute("nonce",d);document.body.appendChild(c);google.psa=!0};google.xjsu=u;setTimeout(function(){m()},0);})();function _DumpException(e){throw e;}
function _F_installCss(c){}
(function(){google.jl={attn:false,blt:'none',chnk:0,dw:false,dwu:true,emtn:0,end:0,ine:false,lls:'default',pdt:0,rep:0,snet:true,strt:0,ubm:false,uwp:true};})();(function(){var pmc='{\x22d\x22:{},\x22sb_he\x22:{\x22agen\x22:true,\x22cgen\x22:true,\x22client\x22:\x22heirloom-hp\x22,\x22dh\x22:true,\x22dhqt\x22:true,\x22ds\x22:\x22\x22,\x22ffql\x22:\x22zh-TW\x22,\x22fl\x22:true,\x22host\x22:\x22google.com\x22,\x22isbh\x22:28,\x22jsonp\x22:true,\x22msgs\x22:{\x22cibl\x22:\x22&#28165;&#38500;&#25628;&#23563;\x22,\x22dym\x22:\x22&#20320;&#26159;&#19981;&#26159;&#35201;&#26597;&#65306;\x22,\x22lcky\x22:\x22&#22909;&#25163;&#27683;\x22,\x22lml\x22:\x22&#30637;&#35299;&#35443;&#24773;\x22,\x22oskt\x22:\x22&#36664;&#20837;&#24037;&#20855;\x22,\x22psrc\x22:\x22&#24050;&#24478;&#24744;&#30340;&#12300;\\u003Ca href\x3d\\\x22/history\\\x22\\u003E&#32178;&#38913;&#35352;&#37636;\\u003C/a\\u003E&#12301;&#20013;&#31227;&#38500;&#36889;&#31558;&#25628;&#23563;&#35352;&#37636;\x22,\x22psrl\x22:\x22&#31227;&#38500;\x22,\x22sbit\x22:\x22&#20197;&#22294;&#25628;&#23563;\x22,\x22srch\x22:\x22Google &#25628;&#23563;\x22},\x22ovr\x22:{},\x22pq\x22:\x22\x22,\x22refpd\x22:true,\x22rfs\x22:[],\x22sbas\x22:\x220 3px 8px 0 rgba(0,0,0,0.2),0 0 0 1px 
rgba(0,0,0,0.08)\x22,\x22sbpl\x22:16,\x22sbpr\x22:16,\x22scd\x22:10,\x22stok\x22:\x22ovTP1BZS50sAK5UGB4nC-7aGTic\x22,\x22uhde\x22:false}}';google.pmc=JSON.parse(pmc);})();
  </script>
 </body>
</html>
'''
