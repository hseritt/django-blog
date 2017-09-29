/**
 *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
 *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
 */

var disqus_config = function () {
    this.page.url = "http://dev.prodigi.us";  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = "harlinseritt"; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
(function() {  // REQUIRED CONFIGURATION VARIABLE: EDIT THE SHORTNAME BELOW
    var d = document, s = d.createElement('script');
    
    s.src = 'https://dev-prodigi-us.disqus.com/embed.js';  // IMPORTANT: Replace EXAMPLE with your forum shortname!
    
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
})();
