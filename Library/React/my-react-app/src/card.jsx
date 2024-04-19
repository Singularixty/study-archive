import ProFilePic from './assets/sample-pf.jpg'
function Card(){
    return(
        <div className="card">
            <img className='card-pic' src={ProFilePic} alt="Profile Picture"/>
            <h2 className='card-title'>Singularixty</h2>
            <p>Student Developer</p>
        </div>
    );
}

export default Card