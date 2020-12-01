(this.webpackJsonpfront=this.webpackJsonpfront||[]).push([[0],{107:function(e,t,a){},126:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),l=a(24),o=a.n(l),s=(a(89),a(17)),c=a(8),i=a(12),u=a(15),m=a.n(u),d=(a(107),a(44)),p=a(43),h=a(80),g=a(27);var f=function(){var e=Object(n.useState)(!1),t=Object(i.a)(e,2),a=t[0],l=t[1];return Object(n.useEffect)((function(){m.a.get("/login",{withCredentials:!0}).then((function(e){console.log("loginGET:"+e.status),console.log(e),200===e.status?l(!0):205===e.status&&l(!1)})).catch((function(e){console.log("loginGET:"+e.response.status),console.log(e.response)}))}),[]),console.log(a),r.a.createElement(d.a,{bg:"light",expand:"lg"},r.a.createElement(d.a.Brand,{href:"/ihomie"},"iHomie"),r.a.createElement(d.a.Toggle,{"aria-controls":"basic-navbar-nav"}),r.a.createElement(d.a.Collapse,{id:"basic-navbar-nav"},r.a.createElement(p.a,{className:"mr-auto"},r.a.createElement(p.a.Link,{href:"/ihomie"},"Home"),r.a.createElement(p.a.Link,{href:"/ihomie#/upload"},"Upload"),r.a.createElement(p.a.Link,{href:"/ihomie#/register"},"Register")),r.a.createElement(h.a,{inline:!0},0==a?r.a.createElement(g.a,{variant:"outline-primary",onClick:function(e){window.location="/ihomie#/login"}},"Login"):r.a.createElement(g.a,{variant:"primary",onClick:function(e){m.a.get("/logout",{withCredentials:!0}).then((function(e){console.log("logoutGET:"+e.status),console.log(e),200===e.status&&l(!1)})).catch((function(e){console.log("logoutGET:"+e.response.status),console.log(e.response)}))}},"Logout"))))},E=a(131),b=a(130);var v=function(){var e=Object(n.useState)([]),t=Object(i.a)(e,2),a=t[0],l=t[1];Object(n.useEffect)((function(){m.a.get("/housings").then((function(e){console.log(e.data),console.log("housingsGET:"+e.status),l(e.data),console.log(a)}))}),[]);var o=a.map((function(e,t){return r.a.createElement(E.a,{lg:6,md:8,xs:24,style:{border:"#CCC solid 1px","border-radius":"10px",padding:"30px",margin:"30px auto 30px"}},r.a.createElement("img",{style:{width:"100%"},src:"https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg",alt:"houseImage"}),r.a.createElement("p",{style:{"padding-top":"10px",margin:"0","font-size":"24px","font-weight":"700"}},e.name),r.a.createElement("p",{style:{"padding-top":"10px","padding-bottom":"5px",margin:"0"}},e.address),r.a.createElement(s.b,{style:{"padding-top":"10px",margin:"0"},to:{pathname:"/detail",state:{objectId:e._id.$oid}}},"Go to see detail"))}));return r.a.createElement("div",{style:{width:"65%",margin:"3rem auto"}},r.a.createElement("div",{style:{textAlign:"center"}},r.a.createElement("h2",null,"  Find Your Future Home in iHomie ")),r.a.createElement("div",null,r.a.createElement(b.a,{gutter:[16,16]},o)),r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement("div",{style:{display:"flex",justifyContent:"center"}},r.a.createElement(s.b,{className:"link",to:"/upload"},"Upload New House")),r.a.createElement("div",{style:{display:"flex",justifyContent:"center"}},r.a.createElement(s.b,{className:"link",to:"/account_update",style:{color:"orange"}},"Update Account Information")))},y=a(75),w=a(29),C=a.n(w),S=a(53),j=a(76),x=a(77),k=a(82),O=a(81),T=a(78),I=a(79),B=a(37),N=a(31),P=a(39),A=a(30),F=a(42),H=a(58),L=function(e){Object(k.a)(a,e);var t=Object(O.a)(a);function a(e){var n;return Object(j.a)(this,a),(n=t.call(this,e)).state={name:"",address:"",prevState:null,needLogin:!1,show:!1,showSuccessBar:!1,showFailureBar:!1,errorCode:0,goHomePage:!1},n}return Object(x.a)(a,[{key:"componentDidMount",value:function(){var e=Object(S.a)(C.a.mark((function e(){var t;return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("/housings/".concat(this.props.objectId)).then((function(e){return e.json()}));case 2:t=e.sent,this.setState(t);case 4:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"handleInputChange",value:function(e){this.setState(Object(y.a)({},e.target.name,e.target.value))}},{key:"handleModify",value:function(e){this.setState({prevState:this.state,show:!0})}},{key:"handleSave",value:function(){var e=Object(S.a)(C.a.mark((function e(t){var a=this;return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("/housings/".concat(this.props.objectId),{method:"PUT",headers:{"Content-Type":"application/json"},credentials:"include",body:JSON.stringify(this.state)}).then((function(e){405==e.status?a.setState({needLogin:!0}):200==e.status?a.setState({show:!1,showSuccessBar:!0}):(a.state.prevState.showFailureBar=!0,a.state.prevState.errorCode=e.status,a.setState(a.state.prevState))}));case 2:e.sent;case 3:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}()},{key:"handleDelete",value:function(){var e=Object(S.a)(C.a.mark((function e(t){var a=this;return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("/housings/".concat(this.props.objectId),{method:"DELETE",headers:{"Content-Type":"application/json"},credentials:"include"}).then((function(e){405==e.status?a.setState({needLogin:!0}):200==e.status?a.setState({goHomePage:!0}):a.setState({show:!1,showFailureBar:!0,errorCode:e.status})}));case 2:e.sent;case 3:case"end":return e.stop()}}),e,this)})));return function(t){return e.apply(this,arguments)}}()},{key:"handleCancel",value:function(e){this.state.prevState.show=!1,this.setState(this.state.prevState)}},{key:"handleClose",value:function(e){this.setState({show:!1})}},{key:"handleCloseSuccessBar",value:function(e){this.setState({showSuccessBar:!1})}},{key:"handleCloseFailureBar",value:function(e){this.setState({showFailureBar:!1})}},{key:"render",value:function(){var e=this.state,t=e.name,a=e.address,n=e.needLogin,l=e.show,o=e.showSuccessBar,s=e.showFailureBar,i=e.errorCode,u=e.goHomePage;return n?r.a.createElement(c.a,{to:"/login"}):u?r.a.createElement(c.a,{to:"/"}):r.a.createElement(r.a.Fragment,null,r.a.createElement(H.a,{show:o,variant:"success",onClose:this.handleCloseSuccessBar.bind(this),dismissible:!0},"Modified information successfully!"),r.a.createElement(H.a,{show:s,variant:"danger",onClose:this.handleCloseFailureBar.bind(this),dismissible:!0},"Failed to modify information, error response code: ",i),r.a.createElement(P.a,{show:l,onHide:this.handleClose.bind(this)},r.a.createElement(P.a.Header,{closeButton:!0},r.a.createElement(P.a.Title,null,"Modify house information")),r.a.createElement(P.a.Body,null,r.a.createElement(A.a,{className:"mb-3"},r.a.createElement(A.a.Prepend,null,r.a.createElement(A.a.Text,{id:"basic-addon3"},"Name")),r.a.createElement(F.a,{name:"name","aria-describedby":"basic-addon3",value:t,onChange:this.handleInputChange.bind(this)})),r.a.createElement(A.a,{className:"mb-3"},r.a.createElement(A.a.Prepend,null,r.a.createElement(A.a.Text,{id:"basic-addon3"},"Address")),r.a.createElement(F.a,{name:"address","aria-describedby":"basic-addon3",value:a,onChange:this.handleInputChange.bind(this)}))),r.a.createElement(P.a.Footer,null,r.a.createElement(g.a,{variant:"primary",onClick:this.handleSave.bind(this)},"Save Changes"),r.a.createElement(g.a,{variant:"secondary",onClick:this.handleCancel.bind(this)},"Cancel"))),r.a.createElement(T.a,null,r.a.createElement(I.a,null,r.a.createElement(B.a,null),r.a.createElement(B.a,null,r.a.createElement(N.a,{style:{width:"50em",margin:"1em"}},r.a.createElement(N.a.Img,{variant:"top",src:"https://bootstrapmade.com/demo/themes/EstateAgency/assets/img/slide-2.jpg"}),r.a.createElement(N.a.Body,null,r.a.createElement(N.a.Title,null,t),r.a.createElement(N.a.Subtitle,{className:"mb-2 text-muted"},a),r.a.createElement(N.a.Text,null,"A property description is the written portion of a real estate listing that describes the real estate for sale or lease. Nowadays, most buyers begin their property search online. Therefore, real estate descriptions are your best chance to sway buyers and sellers."),r.a.createElement(g.a,{variant:"primary",onClick:this.handleModify.bind(this)},"Modify"),r.a.createElement(g.a,{variant:"primary",onClick:this.handleDelete.bind(this),style:{margin:"1px"}},"Delete")))),r.a.createElement(B.a,null))))}}]),a}(r.a.Component);var D=Object(c.g)((function(e){return r.a.createElement(L,{objectId:e.location.state.objectId})}));var U=function(){var e=Object(n.useState)(""),t=Object(i.a)(e,2),a=t[0],l=t[1],o=Object(n.useState)(""),s=Object(i.a)(o,2),c=s[0],u=s[1];return r.a.createElement("div",null,r.a.createElement("div",{style:{width:"75%",margin:"3rem auto"}},r.a.createElement("form",null,r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"House Name"),r.a.createElement("input",{type:"text",onChange:function(e){l(e.currentTarget.value)},class:"form-control",id:"email-input",placeholder:"Input your email address here"})),r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"Address"),r.a.createElement("input",{type:"text",onChange:function(e){u(e.currentTarget.value)},class:"form-control",id:"password-input",placeholder:"Input your password here"})),r.a.createElement("button",{type:"submit",class:"btn btn-primary",onClick:function(e){if(e.preventDefault(),!a||!c)return alert("Please fill in all fields!");console.log(a),console.log(c);var t={name:a,address:c};m.a.post("/housings",t,{withCredentials:!0}).then((function(e){console.log(e.status),console.log(e),200===e.status?alert("Upload successfully!"):alert("You meet with an error!")}))}},"Submit"))))};var M=function(){var e=Object(n.useState)(""),t=Object(i.a)(e,2),a=t[0],l=t[1],o=Object(n.useState)(""),c=Object(i.a)(o,2),u=c[0],d=c[1];return r.a.createElement("div",{style:{width:"75%",margin:"3rem auto"}},r.a.createElement("form",null,r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"Email address"),r.a.createElement("input",{type:"email",onChange:function(e){l(e.currentTarget.value)},class:"form-control",id:"email-input",placeholder:"Input your email address here"})),r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"Password"),r.a.createElement("input",{type:"password",onChange:function(e){d(e.currentTarget.value)},class:"form-control",id:"password-input",placeholder:"Input your password here"})),r.a.createElement("button",{type:"submit",class:"btn btn-primary",onClick:function(e){if(e.preventDefault(),!a||!u)return alert("Please fill in all fields!");console.log(a),console.log(u);var t={email:a,password:u};console.log(t),m.a.post("/login",t,{withCredentials:!0}).then((function(e){console.log(e.status),console.log(e),200===e.status?(alert("Login successfully!"),window.location.replace("/ihomie")):alert("You meet with an error!")})).catch((function(e){console.log(e.response),401===e.response.status?alert("You need to register for the account!"):400===e.response.status?alert("Wrong Password!"):402===e.response.status&&alert("Wrong Parameters!")}))}},"Submit")),r.a.createElement("small",{class:"text-muted"},"Need An Account? ",r.a.createElement(s.b,{className:"link",to:"/register"},"Sign Up Now")))};var Y=function(){var e=Object(n.useState)(""),t=Object(i.a)(e,2),a=t[0],l=t[1],o=Object(n.useState)(""),c=Object(i.a)(o,2),u=c[0],d=c[1],p=Object(n.useState)(""),h=Object(i.a)(p,2),g=h[0],f=h[1];return r.a.createElement("div",{style:{width:"75%",margin:"3rem auto"}},r.a.createElement("form",null,r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"Username"),r.a.createElement("input",{type:"text",onChange:function(e){l(e.currentTarget.value)},class:"form-control",id:"email-input",placeholder:"Input username here"})),r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"Email address"),r.a.createElement("input",{type:"email",onChange:function(e){d(e.currentTarget.value)},class:"form-control",id:"email-input",placeholder:"Input your email address here"})),r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"Password"),r.a.createElement("input",{type:"password",onChange:function(e){f(e.currentTarget.value)},class:"form-control",id:"password-input",placeholder:"Input your password here"})),r.a.createElement("button",{type:"submit",class:"btn btn-primary",onClick:function(e){if(e.preventDefault(),!a||!u||!g)return alert("Please fill in all fields!");console.log(a),console.log(u),console.log(g);var t={username:a,email:u,password:g};console.log(t),m.a.post("/register",t).then((function(e){console.log(e.status),console.log(e),200===e.status?alert("Register successfully!"):alert("You meet with an error!")})).catch((function(e){console.log(e.response),401===e.response.status?alert("The email has been registered!"):402===e.response.status?alert("This username is unavailable!"):400===e.response.status?alert("You have loged in already!"):403===e.response.status&&alert("Parameter wrong!")}))}},"Submit")),r.a.createElement("small",{class:"text-muted"},"Already Have An Account? ",r.a.createElement(s.b,{className:"link",to:"/login"},"Sign In")))};var G=function(){var e=Object(n.useState)(""),t=Object(i.a)(e,2),a=t[0],l=t[1],o=Object(n.useState)(""),s=Object(i.a)(o,2),c=s[0],u=s[1];return r.a.createElement("div",null,r.a.createElement("div",{style:{width:"75%",margin:"3rem auto"}},r.a.createElement("form",null,r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"User Name"),r.a.createElement("input",{type:"text",onChange:function(e){l(e.currentTarget.value)},class:"form-control",id:"username-input",placeholder:"Input new username here"})),r.a.createElement("div",{class:"form-group"},r.a.createElement("label",null,"Email"),r.a.createElement("input",{type:"text",onChange:function(e){u(e.currentTarget.value)},class:"form-control",id:"email-input",placeholder:"Input new email address here"})),r.a.createElement("button",{type:"submit",class:"btn btn-primary",onClick:function(e){if(e.preventDefault(),!a||!c)return alert("Please fill in all fields!");console.log(a),console.log(c);var t={username:a,email:c};m.a.put("/account",t,{withCredentials:!0}).then((function(e){console.log(e.status),console.log(e),200===e.status?(alert("Account updated successfully!"),window.location.replace("/ihomie")):alert("You meet with an error!")})).catch((function(e){console.log(e.response),401===e.response.status&&alert("This account has existed!")}))}},"Submit"))))};var W=function(){return r.a.createElement("div",{className:"App"},r.a.createElement(s.a,null,r.a.createElement(f,null),r.a.createElement(c.d,null,r.a.createElement(c.b,{exact:!0,path:"/",component:v}),r.a.createElement(c.b,{exact:!0,path:"/detail",component:D}),r.a.createElement(c.b,{exact:!0,path:"/upload",component:U}),r.a.createElement(c.b,{exact:!0,path:"/login",component:M}),r.a.createElement(c.b,{exact:!0,path:"/register",component:Y}),r.a.createElement(c.b,{exact:!0,path:"/account_update",component:G}))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));a(125);o.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(W,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))},84:function(e,t,a){e.exports=a(126)},89:function(e,t,a){}},[[84,1,2]]]);
//# sourceMappingURL=main.64a668f6.chunk.js.map