if ( ! Detector.webgl ) Detector.addGetWebGLMessage();
var camera, cameraTarget, scene, renderer;
init();
animate();
function init() {
	container = document.getElementById("result");
    // container = document.createElement( 'div' );
    document.body.appendChild( container );
    camera = new THREE.PerspectiveCamera( 50, window.innerWidth / window.innerHeight, 0.001, 10000 );
    camera.position.set( 3, 0.15, 3 );
    cameraTarget = new THREE.Vector3( 0, -0.1, 0 );
    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0x72645b );
    // scene.fog = new THREE.Fog( 0x72645b, 2, 15 );

    // PLY file
    var loader = new THREE.PLYLoader();
    loader.load( '/static/ply/' + plyFileName, function ( geometry ) {
    // loader.load( '/static/ply/jesus_nview.ply', function ( geometry ) {
        var material = new THREE.PointsMaterial( { vertexColors: THREE.VertexColors, size: 2, sizeAttenuation: false } );
        var points = new THREE.Points( geometry, material );
        points.position.y = - 2.9;
        points.position.z =   0.3;
        points.rotation.x = - Math.PI / 2;
        points.scale.multiplyScalar( 0.5 );
        scene.add( points );
    } );

    // renderer
    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setPixelRatio( window.devicePixelRatio );
	renderer.setSize( $(container).width(), $(container).height() + 250 );
    // renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.gammaInput = true;
    renderer.gammaOutput = true;
    renderer.shadowMap.enabled = true;

    // controls
    var controls = new THREE.OrbitControls( camera, renderer.domElement );
    controls.maxPolarAngle = Math.PI;
    controls.minDistance = 0.01;
    controls.maxDistance = 15;
    container.appendChild( renderer.domElement );

    // resize
    window.addEventListener( 'resize', onWindowResize, false );
}

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize( window.innerWidth, window.innerHeight );
}
function animate() {
    requestAnimationFrame( animate );
    render();
}
function render() {
    camera.lookAt( cameraTarget );
    renderer.render( scene, camera );
}
