import{o as _,c as u,w as n,a as r,Q as t,b as d,d as w,e as D,f as b,g as h,h as m,r as p,i as $,j as f,k as y,l as k,F as x,m as L,n as C,p as Q,q as B,s as N,t as O}from"./vendor-3be037dc.js";var i=(e,a)=>{const l=e.__vccOpts||e;for(const[o,s]of a)l[o]=s;return l};const T={emits:["toggleDrawer"],setup(e,{emit:a}){return{toggleLeftDrawerLocal:()=>{a("toggleDrawer")}}}},H={href:"#",id:"toolbar_title"},V=d("img",{src:"https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg"},null,-1),q=m(" Title ");function F(e,a,l,o,s,g){return _(),u(h,null,{default:n(()=>[r(t,{dense:"",flat:"",round:"",icon:"menu",onClick:o.toggleLeftDrawerLocal},null,8,["onClick"]),r(D,{shrink:""},{default:n(()=>[d("a",H,[r(w,null,{default:n(()=>[V]),_:1}),q])]),_:1}),r(b),r(t,{dense:"",unelevated:"",color:"white","text-color":"dark",label:"Login",onClick:o.toggleLeftDrawerLocal},null,8,["onClick"])]),_:1})}var P=i(T,[["render",F]]);const S=()=>{const e=p(!1);return{leftDrawerOpen:e,toggleLeftDrawer:()=>{console.log(e.value),e.value=!e.value,console.log(e.value)}}},j={setup(){const{toggleLeftDrawer:e,leftDrawerOpen:a}=S();return{toggleDrawer:()=>e(),leftDrawerOpen:a}}},A={class:"flex justify-end"};function U(e,a,l,o,s,g){return _(),u($,{modelValue:o.leftDrawerOpen,"onUpdate:modelValue":a[0]||(a[0]=c=>o.leftDrawerOpen=c),side:"left",overlay:"",behavior:"mobile",elevated:""},{default:n(()=>[d("div",A,[r(t,{icon:"close",class:"",densed:"",flat:"",round:"",onClick:o.toggleDrawer},null,8,["onClick"])])]),_:1},8,["modelValue"])}var E=i(j,[["render",U]]);const R={components:{Navbar:P,Drawer:E},setup(){const e=p("");return{drawer:e,triggerDrawer:()=>e.value.toggleDrawer()}}};function z(e,a,l,o,s,g){const c=f("Navbar"),v=f("Drawer");return _(),y(x,null,[r(k,{reveal:"",class:"bg-primary text-white"},{default:n(()=>[r(c,{onToggleDrawer:o.triggerDrawer},null,8,["onToggleDrawer"])]),_:1}),r(v,{ref:"drawer"},null,512)],64)}var G=i(R,[["render",z]]);const I={name:"Base",components:{CustomHeader:G},setup(){return{name:p("my name")}}};function J(e,a,l,o,s,g){const c=f("CustomHeader");return _(),u(B,{view:"hHh lpR lFf"},{default:n(()=>[r(c),r(Q,{style:{}},{default:n(()=>[r(L,null,{default:n(()=>[C(e.$slots,"page_content")]),_:3})]),_:3})]),_:3})}var K=i(I,[["render",J]]);const M=m(" Home "),W={class:"q-pa-md q-gutter-sm"},X={setup(e){return(a,l)=>(_(),u(K,null,{page_content:n(()=>[M,d("div",W,[r(t,{color:"white",icon:"menu","text-color":"black",label:"Standard"}),r(t,{color:"primary",icon:"mdi-account-lock",label:"Primary"}),r(t,{color:"secondary",label:"Secondary"}),r(t,{color:"amber",glossy:"",label:"Amber"}),r(t,{color:"brown-5",label:"Brown 5"}),r(t,{color:"deep-orange",glossy:"",label:"Deep Orange"}),r(t,{color:"purple",label:"Purple"}),r(t,{color:"black",label:"Black"})])]),_:1}))}};var Y={plugins:{}};N(X).use(O,Y).mount("#app");
