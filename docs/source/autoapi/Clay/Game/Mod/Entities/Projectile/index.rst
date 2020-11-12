
Projectile Class
================



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Projectile`




Syntax
------

.. code-block:: csharp

    public class Projectile : Entity, IComparable, IAudioSourceInfo, ITargettable





.. dn:class:: Clay.Game.Mod.Entities.Projectile
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Projectile


Fields
------

.. dn:class:: Clay.Game.Mod.Entities.Projectile
    :noindex:
    :hidden:

    .. dn:field:: Clay.Game.Mod.Entities.Projectile._pitchInterpolator



        :rtype: System.Single

        .. code-block:: csharp

            public float _pitchInterpolator



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Projectile
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Projectile._pitchSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float _pitchSpeed { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Projectile._projectileFlags



        :rtype: Clay.Game.Mod.Entities.ProjectileFlags

        .. code-block:: csharp

            public ProjectileFlags _projectileFlags { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Projectile.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Projectile.weaponOwner



        :rtype: Clay.Game.Mod.Entities.Entity

        .. code-block:: csharp

            public Entity weaponOwner { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Projectile
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Projectile.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Projectile.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Projectile.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Projectile.FollowEntity(Clay.Game.Mod.Entities.Entity)



        :type target: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public override void FollowEntity(Entity target)

    .. dn:method:: Clay.Game.Mod.Entities.Projectile.IsPlayerAction()



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool IsPlayerAction()

    .. dn:method:: Clay.Game.Mod.Entities.Projectile.SetPlayerAction(System.Boolean)



        :type isPlayerAction: System.Boolean


        .. code-block:: csharp

            public override void SetPlayerAction(bool isPlayerAction)

    .. dn:method:: Clay.Game.Mod.Entities.Projectile.SetWeaponOwner(Clay.Game.Mod.Entities.Entity)



        :type weaponOwner: Clay.Game.Mod.Entities.Entity


        .. code-block:: csharp

            public void SetWeaponOwner(Entity weaponOwner)



