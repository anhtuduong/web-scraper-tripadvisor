(this.$WP=this.$WP||[]).push(["cjerkd",(e,r)=>{var a,n,i,s,d,o,l,t,c,m,u,g,p,h,b,_,f,v,T,G,I,M,w,C,y,H,S,O,k,N,j,W,x,z,D,P,R,q,A,$,L,B,E,F,K,U,Z,J={iconWrapper:"rjSeK d q",iconWrapperSmall:"ADmrQ d q",iconWrapperMedium:"jOFMI d q _T",connectImg:"VNkBD",connectImgSmall:"uUSkJ",connectImgMedium:"jaoBo _T",icon:"nIvCR d Cj",iconSmall:"gqKUw d Cj",iconMedium:"yNpzT d _T Cj"},V=({onClick:e,size:r="large",fontSize:i="large",allBlack:s,...d})=>{var o=k(),l=A.includes(o),[t]=H(d);return a(z,{variant:"secondary",size:r,onClick:e,fullWidth:!0,...t,children:[n(O,{id:"memx_mw_gating_cta",messages:"Continue with:"})," ",a("div",{className:W({[J.iconWrapperSmall]:"small"===i},{[J.iconWrapperMedium]:"medium"===i},{[J.iconWrapper]:"large"===i}),children:[n(y,{src:s?"/img2/google/GoogleG/black.svg":"/img2/google/GoogleG/1color@3x.png",className:W({[J.connectImgSmall]:"small"===i},{[J.connectImgMedium]:"medium"===i},{[J.connectImg]:"large"===i})}),l&&n(y,{src:"/img2/line/line_color_20.png",className:W({[J.connectImgSmall]:"small"===i},{[J.connectImgMedium]:"medium"===i},{[J.connectImg]:"large"===i})}),n("div",{className:W({[J.iconSmall]:"small"===i},{[J.iconMedium]:"medium"===i},{[J.icon]:"large"===i}),children:n(x,{})})]})]})},Q=(e,r,a,n)=>{var i=encodeURIComponent(e),s=encodeURIComponent(e),d=void 0===n?"":`&c=${n}`;return`https://tripadvisor.onelink.me/dIWJ?af_dp=${i}&af_web_dp=${s}&af_sub1=${r}&af_sub2=true&af_sub3=${a}&pid=website${d}`},X=e=>{var r=P(),{onClick:s,mcid:d}=e,o=D(),l=R(),{path:t}=p(),[c]=H(e),m=i(()=>{r({module:"app_download",action:"app_download_click",context:o}),s&&s(o)},[s,r,o]),u=L(`https://${l}${t}`,d,o,"GatingExperiment");return a(z,{variant:"secondary",size:"large",fullWidth:!0,onClick:m,href:u,...c,children:[n(O,{id:"open_in_the_app",messages:"Open in the app"})," "]})},Y={logoset:"w _Z"},ee=e=>{var r,{theme:a}=e;switch(a){case"green":r="/img2/brand_refresh/Tripadvisor_logoset_solid_green.svg";break;case"cream":r="/img2/brand_refresh/Tripadvisor_logoset_solid_cream.svg"}return n(y,{className:Y.logoset,src:r,alt:""})},er=({headline:e,subheadline:r,...i})=>a("div",{className:S(i),children:[n("div",{className:"sHvwv _T d",children:n(E,{theme:"green"})}),n(C,{variant:"expressive-display-02",marginTop:"spacing-04",children:e}),n(C,{variant:"body-01",marginTop:"spacing-02",children:r})]}),ea=({onShow:e,onContinueWith:r,onOpenInApp:i,mcid:s})=>{var{localize:d}=N(),o=M(e);return n(q,{children:a("div",{ref:o,children:[n(F,{headline:d.string("Sign in or open in our app","hard_gate_hybrid_header"),subheadline:d.string("Read traveler reviews, plus save and compare your favorite picks.","hard_gate_subheader")}),n($,{size:"large",onClick:r,fontSize:"medium",marginTop:"spacing-04"}),n(B,{mcid:s,onClick:i,marginTop:"spacing-03"})]})})},en=()=>{},ei=({onShow:e,onDismiss:r,onAutoCancelled:i,onSuccessfulLogin:t,onGeneralSkipDismiss:c,onNotVisible:u,onOneTapHidden:h})=>{var{page:b}=p(),_=g(),{localize:f}=N(),v=M(e),[T,G]=s(null),[I,C]=s(!1),y=es(T),H=d(null);return o(()=>I?(clearTimeout(H.current),()=>{}):(H.current=setTimeout(()=>{!y&&u&&(T?u("hidden"):u("not_mounted"))},3e3),()=>{clearTimeout(H.current)}),[u,T,y,I]),o(()=>{y&&!I?C(!0):!y&&I&&h&&h()},[y,I,C,h]),a(w,{children:[n(l,{children:n(U,{onDismiss:()=>{r&&r(),m(_)},triggerNext:en,onAutoCancelled:i||en,enhancedGoogleOneTapGate:!0,servletName:b,suppressContextualMessage:!0,onSuccessfulLogin:t,onGeneralSkipDismiss:c,onIFrameShown:G})}),n("div",{ref:v,children:n(F,{headline:f.string("Sign in to unlock your free membership","hard_gate_onetap_header"),subheadline:f.string("Read traveler reviews, plus save and compare your favorite picks.","hard_gate_subheader")})})]})},es=e=>{var[r,a]=s(!1);return o(()=>{if(e instanceof HTMLElement){var r=new IntersectionObserver(([e])=>a(e.isIntersecting));return r.observe(e),()=>{r.disconnect()}}return a(!1),()=>{}},[e]),r},ed=({onLogin:e})=>{var{login:r}=c(),d=g(),{page:o}=p(),{geoId:l,locationId:t}=b(),m=_(),{impressionKey:w}=f(),C=v(),y=T(),H=G(15e3,"MembershipHardGateBounce15s"),S=G(3e4,"MembershipHardGateBounce30s"),[O,k]=s(!u(d)),[N,j]=s(!1),W=i(()=>{H(),S()},[H,S]),x=M(W),z=i(()=>{r({flowOrigin:"login",pid:40620,flow:"CORE_COMBINED",isFullWidthMobile:!0,forceLogin:!0,closeX:!1,extraQueryParams:{funnelKey:w,page:o,geo_id:l,detail_id:t,is_dated:m}}).then(e=>{e&&C("MembershipHardGateHybrid",{userId:e.userId,newMember:!!e.hasCreatedMember,source:I(e.loginProvider)},"SuccessLogin",e.userId||void 0)}).finally(e)},[r,e,w,o,l,t,m,C]);return n("div",{ref:x,className:"MmTOI D t _U s l Za f Pk PY Px PK Gg",children:a("div",{className:"KjOWP _Z w f",children:[n("div",{className:"Mbtbi f",children:N&&O&&n(h,{onClick:()=>k(!1)})}),n("div",{className:"ZgpFj f _Z",children:O?n(Z,{onShow:()=>{C("MembershipHardGateGOT")},onDismiss:()=>{y("MembershipHardGateGOT","Close"),k(!1)},onAutoCancelled:()=>{y("MembershipHardGateGOT","Close","other"),k(!1)},onSuccessfulLogin:(r,a)=>{C("MembershipHardGateGOT",{userId:a,newMember:r,source:"google"},"SuccessLogin",a),e&&e()},onGeneralSkipDismiss:(e,r)=>{C("MembershipHardGateGOT",{googleOneTapActionType:e,googleOneTapReason:r},"Error")},onNotVisible:e=>{C("MembershipHardGateGOT",{googleOneTapActionType:"not_visible",googleOneTapReason:e},"Error"),k(!1)},onOneTapHidden:()=>{j(!0)}}):n(K,{onShow:()=>{C("MembershipHardGateHybrid")},onContinueWith:()=>{y("MembershipHardGateHybrid","CTA","click","continueWith"),z()},onOpenInApp:e=>{y("MembershipHardGateHybrid","CTA","click","openInTheApp",{downloadId:e})},mcid:65389})})]})})};return[()=>{A=j(["id-ID","ja-JP","zh-TW","th-TH"]),$=V,L=Q,B=X,E=ee,F=er,K=ea,U=t(()=>r("j3bsmh")),Z=ei,e("default",ed)},[e=>(a=e.jsxs,n=e.jsx),e=>(i=e.useCallback,s=e.useState,d=e.useRef,o=e.useEffect,l=e.Suspense,t=e.lazy),e=>c=e.default,e=>(m=e.setRegDialogDismissed,u=e.shouldSuppressRegistrationDialog),e=>g=e.useSessionId,e=>p=e.useRoute,e=>h=e.CloseButton,e=>(b=e.useRouteIds,_=e.useIsDated,f=e.useHardGateContext,v=e.useHardGateImpression,T=e.useHardGateInteraction,G=e.useBounceTracking,I=e.sourceFromLoginProvider),e=>M=e.useOnVisible,e=>w=e.ErrorBoundary,e=>C=e.default,e=>y=e.CdnImage,e=>(H=e.getMarginProps,S=e.margin),e=>(O=e.default,k=e.useLocale,N=e.useLocalize),e=>j=e.readOnly,e=>W=e.default,e=>x=e.default,e=>z=e.default,e=>D=e.uuid,e=>P=e.useGARecorder,e=>R=e.useDomainName,e=>q=e.AutoFocus]]},["21h32l","o4yt4q","rdycz1","cyrz7y","al4vil","fgwvq1","uzmmz7","igyuz7","3btuy0","83pm0d","essqvy","s6q22n","gw8uw6","7thqz4","5vmpsm","fkji80","gjtatx","jppfwt","eww825","32pwc7","qlcuu5","2r4qug"]]);
