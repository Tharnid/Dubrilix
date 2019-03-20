using System.ComponentModel.DataAnnotations;

namespace DatingApp.API.Dtos
{
    public class UserForRegisterDTO // Data Transfer Object - carries Data between objects
    {
        [Required]
        public string Username { get; set; }
        [Required]
        [StringLength(8, MinimumLength= 5, ErrorMessage="You must specify password between 5 and 8 characters")]
        public string Password { get; set; }
    }
}