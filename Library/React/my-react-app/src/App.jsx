import Header from './Header.jsx'
import Footer from './Footer.jsx'
import Food from './Food.jsx'
import Card from './card.jsx'
import Button from './button/Button.jsx'
import InlineStyleButton from './Inlinecss.jsx'
import Student from './student.jsx'
import UserGreeting from './UserGreet.jsx'
function App() {
  return(
    <>
    <Header/>
    <Card/>
    <Card/>
    <Card/>
    <InlineStyleButton/>
    <Button/>
    <Footer/>
    <Student name="Singularixty:D" age={30} Student={true}/>
    <Student name="RobloxPro" />
    <UserGreeting isLoggedIn={false} username="Singularixty"/>
    </>
  );
}

export default App
