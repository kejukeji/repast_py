/**
 * Created by K on 3/24/14.
 */
$(document).ready(function(){
   document.addEventListener('WeixinJSBridgeReady', function onBridgeReady() {
       WeixinJSBridge.call('showToolbar');
    });

});