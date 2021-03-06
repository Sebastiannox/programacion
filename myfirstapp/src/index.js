//const element = document.createElement('h1')
//element.innerText = 'hello react' /*metodo para agtregar texto a un elemento html creado aqui*/
//const container = document.getElementById('root')
//container.appendChild(element)
import React from "react";
import ReactDOM, { render } from "react-dom";
import {ListPaddockManagerIds, ListPaddockManagersByName} from "./index2";
const container = document.getElementById("root"); //estas llamando a un elemento html de unan pagina html por su id, en este caso, un container
//const user = {
//firstName: 'sebastian',
//lastNmae: 'suazo'
//}
//function getName(user){
//if (true) {
//return `${user.firstName} ${user.lastNmae}`
//}
//}
//function getGreeting(user) {
//if (user) {
//return <h1>hola react {getName(user)}</h1>
//} else {
//return <h1>hola estraño</h1>
//}
//}
//function Deprueba(props) {
//return <h1>se recibe el props {props.name}</h1>
//}
/*
const paddockManagers = [
  { id: 1, taxNumber: "132254524", name: "JUAN TAPIA BURGOS" },
  { id: 2, taxNumber: "143618668", name: "EFRAIN SOTO VERA" },
  { id: 3, taxNumber: "78903228", name: "CARLOS PEREZ GONZALEZ" },
  { id: 4, taxNumber: "176812737", name: "ANDRES VIÑALES CIENFUEGOS" },
  { id: 5, taxNumber: "216352696", name: "OSCAR PEREZ ZUÑIGA" },
  { id: 6, taxNumber: "78684747", name: "JOAQUIN ANDRADE SANDOVAL" },
];
const paddockType = [
  { id: 1, name: "PALTOS" },
  { id: 2, name: "AVELLANOS" },
  { id: 3, name: "CEREZAS" },
  { id: 4, name: "NOGALES" },
];

const farms = [
  { id: 1, name: "AGRICOLA SANTA ANA" },
  { id: 2, name: "VINA SANTA PAULA" },
  { id: 3, name: "FORESTAL Y AGRICOLA LO ENCINA" },
];
const paddocks = [
  {
    paddockManagerId: 6,
    farmId: 1,
    paddockTypeId: 1,
    harvestYear: 2019,
    area: 1200,
  },
  {
    paddockManagerId: 1,
    farmId: 3,
    paddockTypeId: 4,
    harvestYear: 2019,
    area: 500,
  },
  {
    paddockManagerId: 5,
    farmId: 3,
    paddockTypeId: 2,
    harvestYear: 2020,
    area: 20000,
  },
  {
    paddockManagerId: 2,
    farmId: 2,
    paddockTypeId: 3,
    harvestYear: 2021,
    area: 8401,
  },
  {
    paddockManagerId: 3,
    farmId: 1,
    paddockTypeId: 1,
    harvestYear: 2020,
    area: 2877,
  },
  {
    paddockManagerId: 5,
    farmId: 2,
    paddockTypeId: 2,
    harvestYear: 2017,
    area: 15902,
  },
  {
    paddockManagerId: 3,
    farmId: 3,
    paddockTypeId: 2,
    harvestYear: 2018,
    area: 1736,
  },
  {
    paddockManagerId: 2,
    farmId: 3,
    paddockTypeId: 3,
    harvestYear: 2020,
    area: 2965,
  },
  {
    paddockManagerId: 4,
    farmId: 3,
    paddockTypeId: 4,
    harvestYear: 2018,
    area: 1651,
  },
  {
    paddockManagerId: 5,
    farmId: 1,
    paddockTypeId: 1,
    harvestYear: 2018,
    area: 700,
  },
  {
    paddockManagerId: 1,
    farmId: 2,
    paddockTypeId: 1,
    harvestYear: 2019,
    area: 7956,
  },
  {
    paddockManagerId: 5,
    farmId: 3,
    paddockTypeId: 2,
    harvestYear: 2020,
    area: 3745,
  },
  {
    paddockManagerId: 6,
    farmId: 1,
    paddockTypeId: 3,
    harvestYear: 2021,
    area: 11362,
  },
  {
    paddockManagerId: 2,
    farmId: 3,
    paddockTypeId: 3,
    harvestYear: 2021,
    area: 300,
  },
  {
    paddockManagerId: 3,
    farmId: 2,
    paddockTypeId: 2,
    harvestYear: 2020,
    area: 19188,
  },
  {
    paddockManagerId: 3,
    farmId: 1,
    paddockTypeId: 1,
    harvestYear: 2019,
    area: 17137,
  },
  {
    paddockManagerId: 4,
    farmId: 3,
    paddockTypeId: 2,
    harvestYear: 2020,
    area: 100,
  },
  {
    paddockManagerId: 2,
    farmId: 1,
    paddockTypeId: 3,
    harvestYear: 2019,
    area: 11845,
  },
  {
    paddockManagerId: 5,
    farmId: 2,
    paddockTypeId: 1,
    harvestYear: 2018,
    area: 15969,
  },
  {
    paddockManagerId: 1,
    farmId: 3,
    paddockTypeId: 1,
    harvestYear: 2029,
    area: 10420,
  },
  {
    paddockManagerId: 5,
    farmId: 2,
    paddockTypeId: 3,
    harvestYear: 2010,
    area: 3200,
  },
  {
    paddockManagerId: 6,
    farmId: 1,
    paddockTypeId: 2,
    harvestYear: 2012,
    area: 10587,
  },
  {
    paddockManagerId: 2,
    farmId: 2,
    paddockTypeId: 2,
    harvestYear: 2018,
    area: 16750,
  },
];

function ListPaddockManagerIds() {
  return paddockManagers.map((paddockManager) => paddockManager.id);
};
*/
function FormattedDate(props) {
  return <h2>It is {props.date.toLocaleTimeString()}.</h2>;
} //este componente recibiría date en sus props y no sabrá si vino del del estado de Clock, los props de Clock o se definion manualmente
function WarningBanner(props) {
  if (!props.warn) {
    return null;
  } else {
    return (
      <div className="warning" style={{ backgound_color: "red" }}>
        Warning!
      </div>
    );
  }
}
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    //console.log(this);
    this.state = { isToggleOn: true };
    this.handleClick = this.handleClick.bind(this); // enlazamiento necesario para que this funcione en el llamado de lo contrario this será undefined
  }
  handleClick() {
    this.setState((prevState) => ({
      isToggleOn: !prevState.isToggleOn,
    }));
  }
  render() {
    return (
      <div>
        <WarningBanner warn={this.state.isToggleOn} />
        <button onClick={this.handleClick}>
          {this.state.isToggleOn ? "Hide" : "Show"}
        </button>
      </div>
    );
  }
}
class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    this.state = { isLoggedIn: false };
  }

  handleLoginClick() {
    this.setState({ isLoggedIn: true });
  }

  handleLogoutClick() {
    this.setState({ isLoggedIn: false });
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    let button;
    <div>
      {isLoggedIn
        ? (button = <LogoutButton onClick={this.handleLogoutClick} />)
        : (button = <LoginButton onClick={this.handleLoginClick} />)}
    </div>;
    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
        {button}
        <p>
          The user is <b>{isLoggedIn ? "currently" : "not"}</b> logged in.
        </p>
      </div>
    );
  }
}
function UserGreeting(props) {
  return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
  return <h1>Please sign up.</h1>;
}

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

function LoginButton(props) {
  return <button onClick={props.onClick}>Login</button>;
}

function LogoutButton(props) {
  return <button onClick={props.onClick}>Logout</button>;
}
function MailBox(props) {
  const unreadMessages = props.unreadMessages;
  console.log(unreadMessages.length);
  return (
    <div>
      <h1>Hello!</h1>
      {unreadMessages.length > 0 && (
        <h2>you have {unreadMessages.length} unread messages.</h2>
      )}
    </div>
  );
}

const messages = ["React", "Re: React", "Re:Re: React"];
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      date: new Date(),
      //posts: [],
      //comments: []
    }; //se pueden establecer variables independientes en el state
  } //en este constructor añadimos el date de las props al state inicial
  componentDidMount() {
    //se ejecuta despues que la salida del componente se rederiza en el DOM, aqui va el temporizador
    //fetchPosts().then(response=>{
    //this.setState({
    //posts: response.posts
    //});
    //});
    this.timerID = setInterval(() => this.tick(), 1000);
    //this.timerID guarda la ID del temporizador
    //fetchComments().then(response =>{
    //this.setState({
    //comments: response.comments
    //});
    //});
  }
  componentWillUnmount() {
    //al eliminar el DOM de Clock entra en obra este metodo
    clearInterval(this.timerID); //temporizador eliminado
  }
  tick() {
    this.setState({
      date: new Date(),
    }); //este metodo se usará para programar actualizaciones al estado local del componente
  }

  //los dos de arriba se llaman metodos de vida, para cuando un componente se monta y desmonta para ser mas espcifico
  render() {
    return (
      <div>
        <Toggle />
        <FormattedDate date={this.state.date} />
        <LoginControl />
        <MailBox unreadMessages={messages} />
        <ListPaddockManagerIds/>
        <br/>
        <ListPaddockManagersByName/>
      </div>
    ); //de donde recibió el date?? del estado Clock? de las props de Clock?? se definió localmente?? el componente jamás lo sabrá :)
  }
}

/*
function App() {
  return(
    <div>
      <Clock/>
      <Clock/>
      <Clock/>
    </div>
  );
}
*/

ReactDOM.render(<Clock />, container); //metodo para llevar un elemento a alguna otro elemento
//en vez de usar los metodos usuales de javascript o jquery usamos reactDom para manejar el dominio
//function Element(){
//  return(
//    <div>
//      <Deprueba name="sebas"/>
//      <Deprueba name="panchos"/>
//     <Deprueba name="nachita"/>
//   <h2>abajo hay un llamado a una funcion</h2>
// {getGreeting(user)}
//</div> // con las {} concatenas una constante dentro del elemento html creado por jsx
//)
