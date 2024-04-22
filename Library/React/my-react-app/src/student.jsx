import PropTypes from 'prop-types'
function Student(props){
    return(
        <div className="Student">
            <p>Name: {props.name}</p>
            <p>Age: {props.age}</p>
            <p>Student: {props.Student ? "Yes" : "No"}</p>
        </div>
    );
}
Student.defaultProps ={
    name: "Guest",
    age: 0,
    Student: false
}

Student.propTypes = {
    name: PropTypes.string,
    age: PropTypes.number,
    Student: PropTypes.bool
}
export default Student