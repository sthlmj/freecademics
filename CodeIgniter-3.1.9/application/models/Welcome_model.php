class Welcome_model extends CI_Model {
      public $result;

      public function getCategories()
      {
	$result = $this->db->query('SELECT id,name FROM recruting.categories');

	
      }
}