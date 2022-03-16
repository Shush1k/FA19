class Hello extends React.Component {
    render() {
      return <div>
              <p>Имя: {this.props.name}</p>
              <p>Возраст: {this.props.age}</p>
      </div>;
    }
  }
  
  class Clock extends React.Component {
    constructor(props) {
      super(props);
      this.state = {date: new Date()};
    }
  
    componentDidMount() {
      this.timerID = setInterval(
        () => this.tick(),
        1000
      );
    }
  
    componentWillUnmount() {
      clearInterval(this.timerID);
    }
  
    tick() {
      this.setState({
        date: new Date()
      });
    }
  
    render() {
      return (
        <div>
          <h2>Time {this.state.date.toLocaleTimeString()}.</h2>
        </div>
      );
    }
  }

class ClickButton extends React.Component {
             
    constructor(props) {
               super(props);
               this.state = {class: "off", label: "Нажми"};
                  
               this.press = this.press.bind(this);
                  
               console.log("constructor");
           }

           componentDidMount(){
            //    вызывается после рендеринга компонента. Здесь можно выполнять запросы к удаленным ресурсам
               console.log("componentDidMount()");
           }
           componentWillUnmount(){
            //    вызывается перед удалением компонента из DOM
               console.log("componentWillUnmount()");
           }
           shouldComponentUpdate(){
            //    вызывается каждый раз при обновлении объекта props или state. 
            // В качестве параметра передаются новый объект props и state. 
            // Эта функция должна возвращать true (надо делать обновление) или false (игнорировать обновление). 
            // По умолчанию возвращается true. Но если функция будет возвращать false, то тем самым мы отключим обновление компонента,
            // а последующие функции не будут срабатывать.
               console.log("shouldComponentUpdate()");
               return true;
           }
           componentDidUpdate(){
            //    вызывается сразу после обновления компонента (если shouldComponentUpdate возвращает true).
            // В качестве параметров передаются старые значения объектов props и state.
               console.log("componentDidUpdate()");
           }
           press(){
               var className = (this.state.class==="off")?"on":"off";
               this.setState({class: className});
           }
           render() {
               console.log("render()");
               return <button onClick={this.press} className={this.state.class}>{this.state.label}</button>;
           }
}


ReactDOM.render(
    <Hello name="Баранов Александр Вячеславович" age="20" />,
    document.getElementById("fio")
)


ReactDOM.render(
    <ClickButton />,
    document.getElementById("app")
)

ReactDOM.render(
  <Clock />,
  document.getElementById('clock')
);
