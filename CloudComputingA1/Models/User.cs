using System;
using System.ComponentModel.DataAnnotations;

namespace CloudComputingA1.Models
{
	public class EmptyClass
	{
		[Required]
		public string? email { get; set; }
        [Required]
        public string? userName { get; set; }
        [Required]
        public string? password { get; set; }
	
	}
}

